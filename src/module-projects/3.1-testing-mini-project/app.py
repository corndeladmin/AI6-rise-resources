from src.TextClassifier import TextClassifier
import logging
import pandas as pd
from sklearn.model_selection import train_test_split

# Configure basic logging for this application runner
# This is separate from the test logging and shows how you might log application flow
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:
    """
    Demonstrates a simple text classification application flow.
    Initializes, trains, and uses the TextClassifier to make predictions.
    """
    logging.info("Starting the text classification application.")

    # 1. Initialise the TextClassifier
    classifier = TextClassifier()
    logging.info("TextClassifier instance created.")

    # 2. Prepare some training data from the CSV
    try:
        training_df = pd.read_csv("./data/raw/text-label.csv")
        training_texts = training_df["text"].tolist()
        training_labels = training_df["label"].tolist()
        logging.info(f"Loaded {len(training_texts)} training samples from CSV.")

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            training_texts,
            training_labels,
            test_size=0.2,
            random_state=42,
            stratify=training_labels,
        )
        logging.info(
            f"Data split: {len(X_train)} training samples, {len(X_test)} test samples."
        )

    except Exception as e:
        logging.error(f"Error loading training data from CSV: {e}", exc_info=True)
        return  # Exit if data loading fails

    # 3. Train the model
    try:
        classifier.train(X_train, y_train)
        logging.info("Model training successful.")
    except Exception as e:
        logging.error(f"Error during model training: {e}", exc_info=True)
        return

    # 4. Evaluate the model using the test split
    try:
        accuracy = classifier.evaluate(X_test, y_test)
        print(f"\n--- Model Evaluation on Test Set ---")
        print(f"Accuracy: {accuracy:.2f}")
        print("----------------------------------")
        logging.info(f"Model evaluated on test set with accuracy: {accuracy:.2f}")
    except Exception as e:
        logging.warning(f"Could not perform evaluation on test set: {e}")

    # 5. Prepare some new, truly unseen data for prediction (optional, distinct from test set)
    new_texts_for_prediction = [
        "This is an absolutely fantastic product, highly recommended!",
        "I am extremely disappointed with the quality.",
        "It's an average item, nothing special but not bad.",
        "What a great product, I will buy 2 more!",
        "This was a terrible investment, I regret it.",
    ]
    logging.info(
        f"Prepared {len(new_texts_for_prediction)} new samples for prediction."
    )

    # 6. Make predictions on new data
    try:
        predictions = classifier.predict(new_texts_for_prediction)
        logging.info("Predictions generated successfully on new data.")
    except Exception as e:
        logging.error(f"Error during prediction on new data: {e}", exc_info=True)
        return  # Exit if prediction fails

    # 7. Display the prediction results
    print("\n--- Predictions on New Unseen Data ---")
    for i, (text, prediction) in enumerate(zip(new_texts_for_prediction, predictions)):
        print(f"Text {i+1}: '{text}' -> Predicted Sentiment: {prediction.upper()}")
    print("------------------------------------")

    logging.info("Text classification application finished.")


if __name__ == "__main__":
    main()
