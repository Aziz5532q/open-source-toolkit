from open_source_toolkit.json_validator import validate_json
from open_source_toolkit.text_analyzer import analyze_text
from open_source_toolkit.readme_generator import generate_readme


def main():
    print("OPEN SOURCE TOOLKIT")
    print("===================")

    # JSON example
    valid, message = validate_json('{"project": "Toolkit"}')
    print("\nJSON Validator:", message)

    # Text example
    stats = analyze_text("Open source makes development collaborative.")
    print("\nText Analyzer:")
    for name, value in stats.items():
        print(f"{name}: {value}")

    # README example
    readme = generate_readme(
        "Demo Project",
        "A demonstration of Open Source Toolkit.",
        "Ahmed"
    )

    print("\nGenerated README:")
    print(readme)


if __name__ == "__main__":
    main()
