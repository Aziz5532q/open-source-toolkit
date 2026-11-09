"""JSON validation utilities."""

import json
from pathlib import Path


def validate_json(content):
    """Validate JSON text and return (is_valid, message)."""
    try:
        json.loads(content)
        return True, "Valid JSON"
    except json.JSONDecodeError as error:
        return False, f"Invalid JSON: {error}"


def validate_json_file(file_path):
    """Validate a JSON file."""
    path = Path(file_path)

    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return False, f"Could not read file: {error}"

    return validate_json(content)
