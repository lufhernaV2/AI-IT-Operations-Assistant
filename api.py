from fastapi import FastAPI, HTTPException
from ticket_processor import process_ticket
from base_models import Ticket, TicketResponse

app = FastAPI()


tickets_db = {
    1042: {
        "id": 1042,
        "description": "VPN connection failed",
        "priority": "High"
    },
    1043: {
        "id": 1043,
        "description": "Cannot access company email",
        "priority": "Medium"
    }
}



@app.get("/")
def read_root():
    return {"message": "AI IT Operations Assistant is running"}



@app.post(
    "/tickets",
    status_code=201,
    response_model=TicketResponse
)
def create_ticket(ticket: Ticket):

    if ticket.id in tickets_db:
        raise HTTPException(
            status_code=409,
            detail=f"Ticket with ID {ticket.id} already exists"
        )
    # the return below is the response that will be sent 
    # back to the client when a ticket is created
    ticket_data = ticket.model_dump()

    tickets_db[ticket.id] = ticket_data

    processed_message = process_ticket(ticket_data)

    return {
        "ticket_id": ticket.id,
        "message": processed_message,
        # "priority": ticket.priority,
        "status": "received",
        "internal_notes": "This is an internal note and should not be exposed in the response"
    }


@app.get("/tickets/demo/{ticket_id}")
def get_demo_ticket(ticket_id: int):
    if ticket_id != 1042:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "id": 1042,
        "description": "VPN connection failed",
        "priority": "High"
    }


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    ticket = tickets_db.get(ticket_id)

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


