from fastapi import FastAPI
from ticket_processor import process_ticket
from base_models import Ticket

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AI IT Operations Assistant is running"}


@app.post("/tickets")
def create_ticket(ticket: Ticket):
    # the return below is the response that will be sent 
    # back to the client when a ticket is created
    ticket_data = ticket.model_dump()
    processed_message = process_ticket(ticket_data)

    return {
        "ticket_id": ticket.id,
        "message": processed_message,
        # "priority": ticket.priority,
        "status": "received"
    }
