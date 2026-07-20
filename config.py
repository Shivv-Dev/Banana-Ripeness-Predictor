"""
Centralized configuration for the Banalyzer project.

This module contains all project-wide constants, paths,
and configuration settings used throughout the application.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
ASSETS_DIR = PROJECT_ROOT / "assets"
TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"

LOG_DIR = PROJECT_ROOT / "logs"

TRAIN_LOG_DIR = LOG_DIR / "train"

VALIDATION_LOG_DIR = LOG_DIR / "validation"

# Trained model
MODEL_FILENAME = "banana_classifier_final.keras"
MODEL_PATH = MODEL_DIR / MODEL_FILENAME
REPORT_PATH = OUTPUT_DIR / "classification_report.txt"
CONFUSION_MATRIX_PATH = OUTPUT_DIR / "confusion_matrix.png"
CLASS_INDICES_PATH = MODEL_DIR / "class_indices.json"
TRAINING_PLOT_PATH = OUTPUT_DIR / "training_history.png"

for directory in (
    MODEL_DIR,
    OUTPUT_DIR,
    LOG_DIR,
    TRAIN_LOG_DIR,
    VALIDATION_LOG_DIR,
):
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

# Project Metadata
@dataclass(frozen=True)
class ProjectMetadata:
    """Application metadata."""

    name: str
    description: str
    version: str
    author: str
    model_name: str
    model_accuracy: float


PROJECT = ProjectMetadata(
    name="Banalyzer",
    description="Banana Ripeness Prediction using Deep Learning",
    version="1.0.0",
    author="Shivv",
    model_name="MobileNetV2",
    model_accuracy=72.5,
)

# Model Configuration
@dataclass(frozen=True)
class ModelConfig:
    """
    Hyperparameters and inference settings used by the
    MobileNetV2 classification model.
    """

    image_size: int
    batch_size: int
    learning_rate: float
    random_seed: int


MODEL = ModelConfig(
    image_size=224,
    batch_size=16,
    learning_rate=1e-4,
    random_seed=42,
)

# Training Configuration
@dataclass(frozen=True)
class TrainingConfig:
    """Training configuration."""

    epochs: int
    validation_split: float


TRAINING = TrainingConfig(
    epochs=30,
    validation_split=0.20,
)


# Callback Configuration
@dataclass(frozen=True)
class CallbackConfig:
    """Training callback configuration."""

    early_stopping_patience: int
    reduce_lr_patience: int
    reduce_lr_factor: float
    min_learning_rate: float


CALLBACKS = CallbackConfig(
    early_stopping_patience=5,
    reduce_lr_patience=3,
    reduce_lr_factor=0.2,
    min_learning_rate=1e-6,
)

# Dataset Configuration

CLASS_NAMES: tuple[str, ...] = (
    "Overripe",
    "Ripe",
    "Rotten",   
    "Unripe",
)

# Automatically derived from the configured class names.
NUM_CLASSES: int = len(CLASS_NAMES) 

# Prediction Configuration

SUPPORTED_IMAGE_TYPES: tuple[str, ...] = (
    ".jpg",
    ".jpeg",
    ".png",
)


# Backward Compatibility

IMAGE_SIZE = MODEL.image_size
BATCH_SIZE = MODEL.batch_size
LEARNING_RATE = MODEL.learning_rate 
RANDOM_SEED = MODEL.random_seed

EPOCHS = TRAINING.epochs
VALIDATION_SPLIT = TRAINING.validation_split

EARLY_STOPPING_PATIENCE = CALLBACKS.early_stopping_patience
REDUCE_LR_PATIENCE = CALLBACKS.reduce_lr_patience
REDUCE_LR_FACTOR = CALLBACKS.reduce_lr_factor
MIN_LEARNING_RATE = CALLBACKS.min_learning_rate


# color map
PREDICTION_COLORS: dict[str, str] = {
    "Overripe": "#EA580C",
    "Ripe": "#16A34A",
    "Rotten": "#DC2626",
    "Unripe": "#EAB308",
}