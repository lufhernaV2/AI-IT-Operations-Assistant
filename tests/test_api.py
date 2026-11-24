from fastapi.testclient import TestClient
from api import app, tickets_db
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tickets():
    original_tickets = {
        ticket_id: ticket.copy()
        for ticket_id, ticket in tickets_db.items()
    }

    yield

    tickets_db.clear()
    tickets_db.update(original_tickets)



def test_create_ticket_success():
    ticket_data = {
        "id": 1045,
        "description": "VPN connection failed",
        "priority": "High"
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 201
    assert response.json()["ticket_id"] == 1045
    assert response.json()["message"] == "Ticket 1045: VPN connection failed"
    assert response.json()["status"] == "received"



def test_create_ticket_invalid_priority():
    ticket_data = {
        "id": 1043,
        "description": "VPN connection failed",
        "priority": "Urgent"
    }

    response = client.post("/tickets", json=ticket_data)

    # A 422 verifies that the request was unprocessable due to validation errors
    # However, the response will contain details about the validation error, including the field that caused the error and the expected values.
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "literal_error"
    assert response.json()["detail"][0]["loc"] == ["body", "priority"]



def test_create_ticket_duplicate_id():
    ticket_data = {
        "id": 1042,
        "description": "Printer is out of paper",
        "priority": "Low"
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 409
    assert response.json()["detail"] == "Ticket with ID 1042 already exists"

    get_response = client.get("/tickets/1042")

    assert get_response.status_code == 200
    assert get_response.json()["description"] == "VPN connection failed"
    assert get_response.json()["priority"] == "High"


