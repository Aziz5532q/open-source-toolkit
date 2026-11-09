from open_source_toolkit.code_cleaner import find_trailing_whitespace


def test_detect_trailing_spaces():
    content = "hello  \nworld\n"
    assert find_trailing_whitespace(content) == [1]


def test_no_trailing_spaces():
    content = "hello\nworld"
    assert find_trailing_whitespace(content) == []
