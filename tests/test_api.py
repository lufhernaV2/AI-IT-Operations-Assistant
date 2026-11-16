from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_create_ticket_success():
    ticket_data = {
        "id": 1042,
        "description": "VPN connection failed",
        "priority": "High"
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 200
    assert response.json()["ticket_id"] == 1042
    assert response.json()["message"] == "Ticket 1042: VPN connection failed"
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

