from sklearn.metrics import accuracy_score


def test_end_to_end_pipeline_integration(trained_classifier):
    """
    Integration test for the full text classification pipeline.
    Tests data preprocessing, vectorization, and prediction working together.
    Instead of exact prediction match, checks if accuracy is above a threshold.
    """
    # Simulate new raw input data
    new_raw_texts = [
        "This movie was truly fantastic!",
        "I absolutely hated the ending.",
        "It was okay, nothing special.",
        "A brilliant and engaging story.",
        "The best product I've ever used.",
        "Completely awful, do not recommend.",
    ]

    # True labels for the integration test data to calculate accuracy
    true_integration_labels = [
        "positive",
        "negative",
        "positive",
        "positive",
        "positive",
        "negative",
    ]

    # Run the full prediction pipeline to get actual predictions
    actual_predictions = trained_classifier.predict(new_raw_texts)

    # Calculate accuracy for the integration test
    integration_accuracy = accuracy_score(true_integration_labels, actual_predictions)

    # Set a threshold for acceptable integration performance
    expected_min_integration_accuracy = (
        0.65  # Adjust based on expected model performance
    )

    assert (
        integration_accuracy >= expected_min_integration_accuracy
    ), f"Integration test accuracy dropped to {integration_accuracy:.2f}, expected >= {expected_min_integration_accuracy:.2f}"
