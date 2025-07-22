import pytest
import pandas as pd
from src.TextClassifier import TextClassifier


@pytest.fixture(scope="session")
def trained_classifier():
    """
    Fixture to provide a pre-trained classifier for regression/integration tests.
    """
    classifier = TextClassifier()

    training_df = pd.read_csv("./data/raw/text-label.csv")
    texts = training_df["text"].tolist()
    labels = training_df["label"].tolist()

    classifier.train(texts, labels)
    return classifier
