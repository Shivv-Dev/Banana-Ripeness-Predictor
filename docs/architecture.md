# 🏗️ Banalyzer System Architecture

## Overview

Banalyzer is a production-inspired machine learning application that classifies the ripeness stage of bananas from a single image.

The project was designed to demonstrate an end-to-end machine learning workflow while following software engineering principles such as modularity, separation of concerns, centralized configuration, and reusable components.

The architecture separates training, evaluation, inference, and presentation into independent modules, making the project easier to maintain and extend.

---

# 🎯 Design Goals

The project was designed with the following objectives:

- Build an end-to-end computer vision application.
- Keep the architecture modular and maintainable.
- Separate machine learning logic from the user interface.
- Make the prediction pipeline reusable.
- Keep configuration centralized.
- Provide a user-friendly deployment through Streamlit.

---

# 🏛️ High-Level Architecture

```text
                 User
                   │
                   ▼
         Streamlit Web Interface
                   │
                   ▼
          Image Upload Module
                   │
                   ▼
        Image Validation Layer
                   │
                   ▼
       Image Preprocessing Pipeline
                   │
                   ▼
        MobileNetV2 Prediction Engine
                   │
                   ▼
      Probability & Confidence Analysis
                   │
                   ▼
      Prediction Explanation Engine
                   │
                   ▼
        Recommendation Generator
                   │
                   ▼
        Interactive Result Dashboard
```

---

# 📂 Project Structure

```text
Banalyzer/
│
├── assets/
│
├── data/
│   ├── train/
│   └── test/
│
├── docs/
│
├── logs/
│
├── models/
│
├── outputs/
│
├── utils/
│
├── app.py
├── train.py
├── evaluate.py
├── predict.py
├── config.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

Each directory has a single responsibility, reducing coupling between different parts of the project.

---

# 🔄 Prediction Pipeline

The prediction workflow consists of the following stages:

## 1. Image Upload

The user uploads a banana image through the Streamlit interface.

---

## 2. Validation

The application verifies:

- supported file format
- readable image
- valid dimensions

---

## 3. Preprocessing

The image is prepared for inference by:

- resizing to 224 × 224
- RGB conversion
- normalization
- tensor creation

---

## 4. Model Inference

The processed image is passed to the trained MobileNetV2 model.

The model predicts probabilities for all four ripeness classes.

---

## 5. Post-processing

The prediction pipeline calculates:

- predicted class
- confidence score
- probability distribution
- runner-up prediction

---

## 6. Business Logic

Additional insights are generated, including:

- ripeness status
- recommendation
- confidence interpretation
- expected usage

---

## 7. Presentation Layer

The Streamlit interface presents the results through:

- prediction cards
- confidence gauge
- probability bars
- metadata
- lifecycle visualization
- ripeness insights

---

# ⚙️ Configuration Strategy

All configurable values are centralized inside `config.py`.

Examples include:

- model path
- image size
- class labels
- application metadata

Centralizing configuration avoids duplicated constants and improves maintainability.

---

# 🧩 Separation of Responsibilities

| Component | Responsibility |
|-----------|----------------|
| `train.py` | Model training |
| `evaluate.py` | Performance evaluation |
| `predict.py` | Prediction engine |
| `app.py` | User interface |
| `config.py` | Application configuration |
| `utils/` | Shared utilities |

This separation ensures that each module has a clear and focused responsibility.

---

# 📈 Scalability

Although Banalyzer currently focuses on banana ripeness classification, the architecture can be extended to support:

- additional fruit categories
- batch image prediction
- REST API deployment
- cloud inference
- mobile deployment
- model versioning
- explainable AI techniques such as Grad-CAM

The modular design minimizes the effort required to introduce these enhancements.

---

# 💡 Key Engineering Decisions

## MobileNetV2

Chosen for its balance between computational efficiency and predictive performance.

---

## Transfer Learning

Reduces training time while leveraging pre-trained visual features learned from ImageNet.

---

## Streamlit

Provides a lightweight deployment solution with an intuitive interface for interacting with the trained model.

---

## Modular Design

Separating training, inference, evaluation, and presentation improves readability, maintainability, and long-term scalability.

---

# 📌 Summary

Banalyzer demonstrates how machine learning models can be integrated into a production-inspired application through a modular architecture.

Rather than treating model inference as an isolated task, the project combines preprocessing, prediction, confidence analysis, user experience, and deployment into a cohesive system that is easy to understand, maintain, and extend.