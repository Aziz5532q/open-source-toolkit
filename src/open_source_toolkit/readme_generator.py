"""README generation utilities."""


def generate_readme(name, description, author, license_name="MIT"):
    """Generate basic Markdown project documentation."""
    return f"""# {name}

{description}

## Installation

Clone this repository and install its dependencies.

## Usage

Import the tools you need and use them in your Python project.

## Author

{author}

## License

This project is licensed under the {license_name} License.
"""
