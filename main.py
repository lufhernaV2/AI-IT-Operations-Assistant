
def process_ticket(ticket):
    message = f"Ticket {ticket['id']}: {ticket.get('description') or 'No description provided'}"

    return message

def get_ticket_priority(ticket_id: int) -> str:
    if ticket_id == 1042:
        return "High"
    if ticket_id == 1043:
        return "Medium"
    else:
        return "Low"


def get_ticket_id(ticket: dict) -> int | None:
    try:
        ticket_id = ticket["id"]

        if not isinstance(ticket_id, int):
            return None

        return ticket_id

    except KeyError:
        return None


ticket = {"id": "1042"}

try:
    ticket_id = ticket["id"]

    if not isinstance(ticket_id, int):
        print("Invalid ticket ID")

except KeyError:
    print("Missing ticket ID")