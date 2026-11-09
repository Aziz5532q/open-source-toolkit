from open_source_toolkit.text_analyzer import analyze_text


def test_analyze_text():
    result = analyze_text("Hello world. How are you?")

    assert result["words"] == 5
    assert result["characters"] == 25
    assert result["sentences"] == 2
    assert result["lines"] == 1


def test_empty_text():
    result = analyze_text("")

    assert result["words"] == 0
    assert result["characters"] == 0
    assert result["lines"] == 0
