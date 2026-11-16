from ticket_processor import get_ticket_id


def test_get_ticket_id_with_valid_id():
    # Arrange
    ticket = {"id": 1042}

    # Act
    result = get_ticket_id(ticket)

    # Assert
    assert result == 1042

def test_get_ticket_id_with_missing_id():
    # Arrange
    ticket = {"description": "VPN connection failed"}

    # Act
    result = get_ticket_id(ticket)

    # Assert
    assert result is None

def test_get_ticket_id_with_invalid_type():
    # Implement your test here
    # Arrange
    ticket = {"id": "INVALID"}

    result = get_ticket_id(ticket)

    # Assert
    assert result is None

