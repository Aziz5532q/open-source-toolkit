from open_source_toolkit.json_validator import validate_json


def test_valid_json():
    valid, message = validate_json('{"name": "Ahmed"}')
    assert valid is True
    assert message == "Valid JSON"


def test_invalid_json():
    valid, message = validate_json('{"name": }')
    assert valid is False
    assert "Invalid JSON" in message
