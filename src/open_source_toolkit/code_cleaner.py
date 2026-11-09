"""Code formatting inspection utilities."""

from pathlib import Path


def find_trailing_whitespace(content):
    """Return line numbers containing trailing whitespace."""
    issues = []

    for number, line in enumerate(content.splitlines(), start=1):
        if line.rstrip(" \t") != line:
            issues.append(number)

    return issues


def inspect_file(file_path):
    """Inspect a text file for trailing whitespace."""
    path = Path(file_path)

    content = path.read_text(encoding="utf-8")
    issues = find_trailing_whitespace(content)

    return {
        "file": str(path),
        "trailing_whitespace_lines": issues,
        "issue_count": len(issues),
    }
