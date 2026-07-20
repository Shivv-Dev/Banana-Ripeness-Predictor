"""
Banalyzer Training Pipeline

Trains the MobileNetV2 transfer learning model for banana
ripeness classification.

Responsibilities:
- Dataset preparation
- Model construction
- Training
- Validation
- Model persistence
- Training visualization
"""
import os
import json
from config import (
    PROJECT,
    MODEL,
    TRAINING,
    CALLBACKS,
    NUM_CLASSES,
    MODEL_PATH,
    TRAIN_DIR,
    LOG_DIR,
    TRAINING_PLOT_PATH,
    CLASS_INDICES_PATH
)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
  

from utils.logger import get_logger

logger = get_logger(__name__)

def create_datasets() -> tuple:

    train_datagen = keras.preprocessing.image.ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        brightness_range=[0.8, 1.2],
        fill_mode='nearest',
        validation_split=TRAINING.validation_split
    )

    train_dataset = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(
            MODEL.image_size,
            MODEL.image_size,
        ),
        batch_size=MODEL.batch_size,
        class_mode='categorical',
        shuffle=True,
        subset="training",
        seed=MODEL.random_seed
    )

    val_dataset = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(
            MODEL.image_size,
            MODEL.image_size,
        ),
        batch_size=MODEL.batch_size,
        class_mode='categorical',
        shuffle=False,
        subset="validation",
        seed=42
    )
    return train_dataset, val_dataset

def build_model() -> keras.Model:
    """Build MobileNetV2-based transfer learning model - SAME AS YOUR ORIGINAL"""
    
    # Load pre-trained MobileNetV2 (without top classification layer)
    base_model = MobileNetV2(
        input_shape=(
            MODEL.image_size,
            MODEL.image_size,
            3,
        ),
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze base model layers
    base_model.trainable = False

    
    
    # Build complete model - SAME AS YOUR ORIGINAL
    model = keras.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dropout(0.3),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(NUM_CLASSES, activation='softmax')
    ])
    
    # Compile model - SAME AS YOUR ORIGINAL
    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=MODEL.learning_rate
        ),
        loss=tf.keras.losses.CategoricalCrossentropy(
            label_smoothing=0.1
        ),
        metrics=['accuracy']
    )
    
    return model

def plot_training_history(history) -> None:
    """Plot training and validation metrics"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot accuracy
    ax1.plot(history.history['accuracy'], label='Train Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    ax1.grid(True)
    
    # Plot loss
    ax2.plot(history.history['loss'], label='Train Loss')
    ax2.plot(history.history['val_loss'], label='Val Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(TRAINING_PLOT_PATH, dpi=300, bbox_inches="tight")
    plt.close()
    
    logger.info(f"Training history saved to {TRAINING_PLOT_PATH}")

def main() -> None:
    """Main training pipeline."""

    try:
        print("=" * 60)
        print(f"{PROJECT.name} v{PROJECT.version}")
        print("Training Pipeline")
        print("=" * 60)

        # Environment Information
        logger.info(f"TensorFlow Version: {tf.__version__}")

        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            logger.info(f"GPU Detected: {gpus}")
        else:
            logger.info("GPU Detected: None (Training will use CPU)")

        # Load datasets
        logger.info("Loading datasets...")
        train_ds, val_ds = create_datasets()

        logger.info(
            "Training samples: %d",
            train_ds.samples,
        )
        logger.info(f"Validation samples: {val_ds.samples}")
        logger.info(f"Classes: {train_ds.class_indices}")

        # Save class indices
        with open(
            CLASS_INDICES_PATH,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(train_ds.class_indices, f, indent=4)

        logger.info(f"Class indices saved to: {CLASS_INDICES_PATH}")

        # Build model
        logger.info("Building MobileNetV2 model...")
        model = build_model()
        model.summary()

        # Setup callbacks
        callbacks = [
            keras.callbacks.EarlyStopping(
                monitor="val_loss",
                patience=CALLBACKS.early_stopping_patience,
                restore_best_weights=True,
                verbose=1,
            ),
            keras.callbacks.ReduceLROnPlateau(
                monitor="val_loss",
                factor=CALLBACKS.reduce_lr_factor,
                patience=CALLBACKS.reduce_lr_patience,
                verbose=1,
            ),
            keras.callbacks.TensorBoard(
                log_dir=LOG_DIR,
                histogram_freq=1,
            ),
        ]

        # Train model
        logger.info(f"Training model for {TRAINING.epochs} epochs...")

        history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=TRAINING.epochs,
            callbacks=callbacks,
            verbose=1,
        )

        # Evaluate model
        logger.info("Evaluating model...")
        val_loss, val_accuracy = model.evaluate(val_ds)

        logger.info(f"Final Validation Accuracy: {val_accuracy * 100:.2f}%")
        logger.info(f"Final Validation Loss: {val_loss:.4f}")

        # Save final model
        model.save(MODEL_PATH)
        logger.info(f"Final model saved to: {MODEL_PATH}")

        # Plot training history
        logger.info("Generating training plots...")
        plot_training_history(history)

        print("\n" + "=" * 60)
        print("Training Complete!")
        print("=" * 60)
        print(f"\nModel saved to: {MODEL_PATH}")
        print(f"Training plot saved to: {TRAINING_PLOT_PATH}")

    except KeyboardInterrupt:
        logger.warning("Training interrupted by user.")

    except Exception:
        logger.exception("Training failed due to an unexpected error.")

    except FileNotFoundError as exc:
        logger.error("%s", exc)

if __name__ == "__main__":
    main()