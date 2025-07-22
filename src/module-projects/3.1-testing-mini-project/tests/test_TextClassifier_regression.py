from src.TextClassifier import TextClassifier


def test_model_regression_accuracy(trained_classifier):
    """
    Regression test to ensure model accuracy does not drop below a threshold.
    This simulates checking if a code change (e.g., in preprocessing or model params)
    has negatively impacted performance on a known validation set.
    """
    # Example texts and labels for testing
    test_texts = [
        "Absolutely fantastic!",
        "So happy with it.",
        "Worst ever.",
        "Not good.",
        "This is amazing, truly exceptional.",
        "Feeling very upset about this purchase.",
    ]
    true_labels = [
        "positive",
        "positive",
        "negative",
        "negative",
        "positive",
        "negative",
    ]

    # Evaluate current model performance
    current_accuracy = trained_classifier.evaluate(test_texts, true_labels)

    # Set a threshold for acceptable performance.
    # If accuracy drops below this, it indicates a regression.
    expected_min_accuracy = 0.80

    assert (
        current_accuracy >= expected_min_accuracy
    ), f"Model accuracy dropped to {current_accuracy:.2f}, expected >= {expected_min_accuracy:.2f}"
