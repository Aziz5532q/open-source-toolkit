# Open Source Toolkit

A collection of practical, reusable Python utilities designed to simplify everyday software development tasks.

![Tests](https://github.com/Aziz5532q/open-source-toolkit/actions/workflows/tests.yml/badge.svg)

## Features

- File Organizer: Organize files by extension.
- JSON Validator: Validate JSON strings and files.
- Text Analyzer: Calculate words, characters, lines, and sentences.
- Code Cleaner: Detect trailing whitespace.
- README Generator: Generate basic Markdown documentation.

## Requirements

Python 3.10 or newer.

## Installation

Clone the repository:

```bash
git clone https://github.com/Aziz5532q/open-source-toolkit.git
cd open-source-toolkit
```

Install the project:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```python
from open_source_toolkit.json_validator import validate_json
from open_source_toolkit.text_analyzer import analyze_text

valid, message = validate_json('{"hello": "world"}')
print(message)

statistics = analyze_text("Hello open-source community!")
print(statistics)
```

Run the demonstration:

```bash
python examples/example.py
```

## Run Tests

```bash
python -m pytest
```

## Project Structure

- `src/`: Python utilities.
- `tests/`: Automated tests.
- `examples/`: Usage examples.

## Contributing

Contributions, bug reports, suggestions, and improvements are welcome.

Please read CONTRIBUTING.md before submitting a pull request.

## Current Status

Version 0.1.0 — Initial development release.

This project is actively being developed. Features and documentation may change.

## License

MIT License. See LICENSE for details.

## Maintainer

Ahmed Lapointe

GitHub: @Aziz5532q
