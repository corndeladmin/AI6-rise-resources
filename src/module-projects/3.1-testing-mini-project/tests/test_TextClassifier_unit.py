from src.TextClassifier import TextClassifier


def test_preprocess_text_basic():
    """Unit test for basic text preprocessing."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("HELLO WORLD") == "hello world"
    # Test case for mixed case text
    # Test case for punctuation removal
    # Test case for numbers and symbols
    # Test case for leading/trailing spaces and multiple spaces
    # Test case for multiple spaces between words


def test_preprocess_text_empty():
    """Unit test for empty string preprocessing."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("") == ""
