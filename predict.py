"""
Banalyzer Prediction Engine

Provides reusable utilities for loading the trained model,
preprocessing images, running inference, and displaying
prediction results through both the command-line interface
and the Streamlit application.
"""

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import time
import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow import keras
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from config import (
    CLASS_NAMES,
    MODEL,
    MODEL_PATH,
    PROJECT,
)
from utils.logger import get_logger
logger = get_logger(__name__)


# Data Models

@dataclass(frozen=True)
class PredictionResult:
    """
    Stores the result of a banana ripeness prediction.
    """

    predicted_class: str
    confidence: float
    probabilities: dict[str, float]
    inference_time_ms: float = 0.0


# Model Utilities

def load_model() -> keras.Model:
    """
    Load the trained model.

    Returns:
        keras.Model: Loaded TensorFlow model.

    Raises:
        FileNotFoundError: If the model file is missing.
    """

    logger.info("Loading trained model...")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at:\n{MODEL_PATH}\n\n"
            "Please train the model first."
        )

    model = keras.models.load_model(MODEL_PATH)

    logger.info("Model loaded successfully.")

    return model

 
# Image Preprocessing

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Load and preprocess an image for prediction.

    Args:
        image_path: Path to the image.

    Returns:
        Preprocessed image tensor.
    """

    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    logger.info(f"Loading image: {image_path.name}")

    image = Image.open(image_path).convert("RGB")
    
    image = image.resize((MODEL.image_size, MODEL.image_size))

    image_array = np.array(image, dtype=np.float32)

    image_array = preprocess_input(image_array)

    image_array = np.expand_dims(image_array, axis=0)

    logger.info("Image preprocessing completed.")

    return image_array



# Prediction Engine

def predict_image(
    model: keras.Model,
    image_path: str,
) -> PredictionResult:
    """
    Predict banana ripeness from an image.

    Args:
        model: Loaded TensorFlow model.
        image_path: Path to image.

    Returns:
        PredictionResult
    """

    logger.info("Running inference...")

    image = preprocess_image(image_path)

    start_time = time.perf_counter()

    predictions = model.predict(
        image,
        verbose=0,
    )[0]

    inference_time_ms = (
        time.perf_counter() - start_time
    ) * 1000

    predicted_index = int(np.argmax(predictions))

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(predictions[predicted_index])

    probabilities = {
        class_name: float(probability)
        for class_name, probability in zip(
            CLASS_NAMES,
            predictions,
        )
    }

    logger.info(
        f"Prediction completed: "
        f"{predicted_class} "
        f"({confidence:.2%})"
    )

    return PredictionResult(
        predicted_class=predicted_class,
        confidence=confidence,
        probabilities=probabilities,
        inference_time_ms=inference_time_ms,
    )

# Display Utilities

def display_prediction(result: PredictionResult) -> None:
    """
    Display prediction results in the console.

    Args:
        result: Prediction result returned by predict_image().
    """

    print("\n" + "=" * 60)
    print("BANANA RIPENESS PREDICTION")
    print("=" * 60)

    print(f"\nPredicted Class : {result.predicted_class.upper()}")
    print(f"Confidence      : {result.confidence:.2%}")

    print("\nClass Probabilities")
    print("-" * 60)

    for class_name, probability in result.probabilities.items():
        percentage = probability * 100
        bar = "█" * int(percentage / 2)

        print(
            f"{class_name:<12} "
            f"{percentage:6.2f}% "
            f"{bar}"
        )

    print("-" * 60)

    if result.confidence >= 0.90:
        print("Prediction Quality : Excellent")
    elif result.confidence >= 0.75:
        print("Prediction Quality : High")
    elif result.confidence >= 0.60:
        print("Prediction Quality : Moderate")
    else:
        print("Prediction Quality : Low (Model Uncertain)")

    print("=" * 60)

    print(f"Inference Time : {result.inference_time_ms:.2f} ms")

# Command Line Interface

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace containing parsed arguments.
    """

    parser = argparse.ArgumentParser(
        description="Banana Ripeness Predictor"
    )

    parser.add_argument(
        "image",
        type=str,
        help="Path to banana image.",
    )

    return parser.parse_args()


# Main

def main() -> None:
    """
    Main prediction pipeline.
    """

    try:

        print("=" * 60)
        print(f"{PROJECT.name} v{PROJECT.version}")
        print("Prediction Pipeline")
        print("=" * 60)

        args = parse_arguments()

        logger.info("Starting prediction pipeline...")

        model = load_model()

        result = predict_image(
            model=model,
            image_path=args.image,
        )

        display_prediction(result)

        logger.info("Prediction completed successfully.")

    except KeyboardInterrupt:
        logger.warning("Prediction interrupted by user.")

    except FileNotFoundError as exc:
        logger.error("%s", exc)

    except Exception:
        logger.exception(
            "Prediction failed due to an unexpected error."
        )


# Entry Point

if __name__ == "__main__":
    main()