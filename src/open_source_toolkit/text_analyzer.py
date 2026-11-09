"""Text analysis utilities."""


def analyze_text(text):
    """Return basic statistics about a text."""
    words = text.split()
    lines = text.splitlines()

    return {
        "characters": len(text),
        "characters_without_spaces": len("".join(text.split())),
        "words": len(words),
        "lines": len(lines),
        "sentences": sum(text.count(mark) for mark in ".!?"),
    }
