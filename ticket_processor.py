def process_ticket(ticket):
    result = f"Ticket {ticket['id']}: {ticket.get('description') or 'No description provided'}"

    return result

def get_ticket_id(ticket: dict) -> int | None:
    try:
        ticket_id = ticket["id"]

        if not isinstance(ticket_id, int):
            return None

        return ticket_id

    except KeyError:
        return None