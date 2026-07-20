
"""
Banalyzer Model Evaluation

Evaluates the trained MobileNetV2 model using the test dataset
and generates evaluation metrics, classification reports,
and confusion matrix visualizations.
"""
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)
from tensorflow import keras
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from config import (
    PROJECT,
    MODEL,
    CLASS_NAMES,
    MODEL_PATH,
    TEST_DIR,
    REPORT_PATH,
    CONFUSION_MATRIX_PATH
)


# Logging Configuration

from utils.logger import get_logger

logger = get_logger(__name__)


# Dataset

def load_test_dataset() -> DirectoryIterator:
    """Load the test dataset."""

    logger.info("Loading test dataset...")

    test_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input
    )

    dataset = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=(
            MODEL.image_size,
            MODEL.image_size,
        ),
        batch_size=MODEL.batch_size,
        class_mode="categorical",
        shuffle=False,
    )

    logger.info(f"Test samples: {dataset.samples}")

    return dataset


# Model

def load_trained_model() -> keras.Model:
    """Load the trained model."""

    logger.info("Loading model...")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at: {MODEL_PATH}\n"
            "Please train the model first by running train.py."
        )

    model = keras.models.load_model(MODEL_PATH)

    logger.info("Model loaded successfully.")

    return model


# Reports

def save_classification_report(true_classes, predicted_classes) -> None:
    """Generate and save the classification report."""

    report = classification_report(
        true_classes,
        predicted_classes,
        target_names=CLASS_NAMES,
    )

    logger.info("Classification Report:")
    print(report)

    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(report)

    logger.info(
        f"Classification report saved to: {REPORT_PATH}"
    )


def save_confusion_matrix(true_classes, predicted_classes) -> None:
    """Generate and save the confusion matrix."""

    cm = confusion_matrix(
        true_classes,
        predicted_classes,
    )

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=CLASS_NAMES,
    )

    fig, ax = plt.subplots(figsize=(8, 8))

    disp.plot(
        cmap="Blues",
        ax=ax,
        colorbar=False,
    )

    plt.title("Confusion Matrix")

    plt.savefig(
        CONFUSION_MATRIX_PATH,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    logger.info(
        f"Confusion matrix saved to: {CONFUSION_MATRIX_PATH}"
    )


# Evaluation Pipeline

def evaluate_model(model, test_dataset) -> None:
    """Evaluate the trained model."""

    logger.info("Evaluating model...")

    loss, accuracy = model.evaluate(test_dataset)

    logger.info(f"Test Accuracy: {accuracy:.2%}")
    logger.info(f"Test Loss: {loss:.4f}")

    logger.info("Generating predictions...")

    predictions = model.predict(
        test_dataset,
        verbose=0,
    )

    predicted_classes = np.argmax(predictions, axis=1)

    true_classes = test_dataset.classes

    save_classification_report(
        true_classes,
        predicted_classes,
    )

    save_confusion_matrix(
        true_classes,
        predicted_classes,
    )



# Main

def main() -> None:
    """Main evaluation pipeline."""

    try:
        print("=" * 60)
        print(f"{PROJECT.name} v{PROJECT.version}")
        print("Model Evaluation")
        print("=" * 60)

        test_dataset = load_test_dataset()

        model = load_trained_model()

        evaluate_model(
            model,
            test_dataset,
        )

        print("\n" + "=" * 60)
        print("Evaluation Completed Successfully!")
        print("=" * 60)

        print(f"\nClassification Report: {REPORT_PATH}")
        print(f"Confusion Matrix: {CONFUSION_MATRIX_PATH}")

    except KeyboardInterrupt:
        logger.warning("Evaluation interrupted by user.")

    except Exception:
        logger.exception("Evaluation failed due to an unexpected error.")

    except FileNotFoundError as exc:
        logger.error("%s", exc)


if __name__ == "__main__":
    main()