# Known Limitations

## Overview

This document describes the known limitations of the current Banalyzer release.

The objective is to clearly communicate the boundaries of the application, model, and dataset so that users and developers understand the expected behavior of the system.

These limitations are documented intentionally and do not necessarily indicate software defects.

---

# Application Limitations

## Single Image Prediction

The application accepts one image at a time.

Batch prediction is not supported.

---

## Supported Input

The application is designed to classify banana images.

Images without bananas may still produce a prediction because the model always returns the most probable class.

---

## Internet Independence

Banalyzer performs all inference locally.

No cloud inference or external API is required.

---

# Model Limitations

## Closed Classification Problem

The model predicts only one of the following classes:

- Unripe
- Ripe
- Overripe
- Rotten

Images outside these categories cannot be classified separately.

---

## Confidence Does Not Guarantee Correctness

A high confidence score indicates that the model strongly prefers one class over the others.

It does not guarantee that the prediction is correct.

---

## Training Dataset Dependency

Prediction quality depends on the diversity and quality of the training dataset.

Images that differ significantly from the training distribution may reduce prediction accuracy.

---

# Image Limitations

Prediction quality may decrease under challenging conditions, including:

- Poor lighting
- Heavy shadows
- Motion blur
- Background clutter
- Partial occlusion
- Extreme camera angles
- Very low image quality

---

# Out-of-Distribution Inputs

The application is not designed to detect whether an uploaded image actually contains a banana.

Non-banana images will still receive one of the supported ripeness classifications.

---

# Hardware Variability

Inference time varies depending on the execution environment.

Factors include:

- CPU
- GPU
- Available memory
- TensorFlow optimizations
- Operating system

Therefore, inference time should not be interpreted as a fixed benchmark.

---

# Scope

The current version intentionally excludes:

- Video inference
- Live camera prediction
- Multiple banana detection
- Object detection
- Shelf-life estimation
- Fruit freshness forecasting
- Mobile deployment
- Cloud inference

These exclusions are part of the project's defined scope rather than software limitations.