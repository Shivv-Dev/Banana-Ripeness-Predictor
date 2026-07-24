"""
Image Validation Engine

Validates whether an uploaded image contains a banana before
running ripeness prediction.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from PIL import Image
from tensorflow import keras
from tensorflow.keras.applications.efficientnet import (
    EfficientNetB0,
    decode_predictions,
    preprocess_input,
)


# ------------------------------------------------------------------
# Data Models
# ------------------------------------------------------------------

@dataclass(frozen=True)
class ValidationResult:
    """
    Result returned by the image validation engine.
    """

    is_valid: bool
    label: str
    confidence: float
    message: str


# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------

BANANA_LABELS = {
    "banana",
    "plantain",
}


# ------------------------------------------------------------------
# Model Utilities
# ------------------------------------------------------------------

def load_validator() -> keras.Model:
    """
    Load the pretrained ImageNet validation model.

    Returns
    -------
    keras.Model
        EfficientNetB0 pretrained on ImageNet.
    """

    return EfficientNetB0(weights="imagenet")


# ------------------------------------------------------------------
# Image Preprocessing
# ------------------------------------------------------------------

def preprocess_validation_image(
    image: Image.Image,
) -> np.ndarray:
    """
    Preprocess an image for EfficientNet inference.
    """

    image = image.convert("RGB")
    image = image.resize((224, 224))

    image_array = np.asarray(image, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)

    return image_array


# ------------------------------------------------------------------
# Validation Engine
# ------------------------------------------------------------------

def validate_image(
    validator: keras.Model,
    image: Image.Image,
) -> ValidationResult:
    """
    Validate whether the uploaded image contains a banana.

    Parameters
    ----------
    validator
        Loaded EfficientNet model.

    image
        Uploaded PIL image.

    Returns
    -------
    ValidationResult
    """

    image_array = preprocess_validation_image(image)

    predictions = validator.predict(
        image_array,
        verbose=0,
    )

    decoded_predictions = decode_predictions(
        predictions,
        top=5,
    )[0]

    for _, label, confidence in decoded_predictions:

        normalized_label = (
            label
            .lower()
            .replace("_", " ")
        )

        if any(
            banana_label in normalized_label
            for banana_label in BANANA_LABELS
        ):
            return ValidationResult(
                is_valid=True,
                label=normalized_label,
                confidence=float(confidence),
                message="Banana detected.",
            )

    top_label = (
        decoded_predictions[0][1]
        .lower()
        .replace("_", " ")
    )

    top_confidence = float(decoded_predictions[0][2])

    return ValidationResult(
        is_valid=False,
        label=top_label,
        confidence=top_confidence,
        message="No banana detected. Please upload a banana image.",
    )