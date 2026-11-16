from ticket_processor import process_ticket, get_ticket_id


def get_ticket_priority(ticket_id: int) -> str:
    if ticket_id == 1042:
        return "High"
    if ticket_id == 1043:
        return "Medium"
    else:
        return "Low"



tickets = [
    {
        "id": 1042,
        "description": "VPN connection failed",
        "priority": "High"
    },
    {
        "id": 1043,
        "description": "Printer not working",
        "priority": "Low"
    },
    {
        "id": 1044,
        "description": "Cannot access company email",
        "priority": "Medium"
    },
    {
        "id": "INVALID",
        "description": "Unable to log in",
        "priority": "High"
    }
]

for ticket in tickets:
    ticket_id = get_ticket_id(ticket)

    if ticket_id is None:
        print("Invalid ticket ID")
        continue
    processed_ticket = process_ticket(ticket)
    print(processed_ticket)


#     ticket_id = ticket["id"]

#     if not isinstance(ticket_id, int):
#         print("Invalid ticket ID")

# except KeyError:
#     print("Missing ticket ID")