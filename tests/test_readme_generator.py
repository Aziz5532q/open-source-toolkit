from open_source_toolkit.readme_generator import generate_readme


def test_generate_readme():
    result = generate_readme(
        "My Project",
        "A useful developer tool.",
        "Ahmed"
    )

    assert "# My Project" in result
    assert "A useful developer tool." in result
    assert "Ahmed" in result
    assert "MIT" in result
