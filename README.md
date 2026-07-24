# Banalyzer

## AI-Powered Banana Ripeness Classification

> Production-inspired Deep Learning application for banana ripeness classification using TensorFlow, MobileNetV2, and Streamlit.

Banalyzer is a computer vision application that classifies banana ripeness from a single image using a MobileNetV2-based deep learning model. The application predicts one of four ripeness stages: Unripe, Ripe, Overripe, or Rotten.

The project was developed to demonstrate an end-to-end machine learning workflow, covering dataset preparation, model training, evaluation, inference, and deployment through an interactive Streamlit application.

Beyond model development, Banalyzer emphasizes software engineering practices such as modular architecture, centralized configuration, structured logging, reusable inference pipelines, and maintainable project organization, reflecting the design principles commonly used in production-oriented AI applications.

---

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-FF6F00?style=for-the-badge&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![MobileNetV2](https://img.shields.io/badge/Model-MobileNetV2-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
[![Live Demo](https://img.shields.io/badge/Live-Demo-Online-success?style=for-the-badge&logo=streamlit)](https://banana-ripeness-predictor.streamlit.app) 
![Version](https://img.shields.io/badge/Version-v1.1.0-blue?style=for-the-badge)

## Project Snapshot

| Property | Value |
|----------|-------|
| Version | v1.1.0 |
| Language | Python 3.13 |
| Framework | TensorFlow 2.20 |
| Model | MobileNetV2 |
| Classes | 4 |
| Accuracy | 72.5% |
| Deployment | Streamlit |
| License | MIT |




## 🌐 Live Demo

Experience Banalyzer directly in your browser without any installation.

**🔗 Live Application:**  
**🚀 Live Demo:** [Open Banalyzer](https://banana-ripeness-predictor.streamlit.app)

> Upload a banana image and receive a ripeness prediction powered by a MobileNetV2 deep learning model.


## Table of Contents

- [🌐 Live Demo](#-live-demo)
- [📖 Overview](#overview)
- [💡 Why Banalyzer?](#-why-banalyzer)
- [✨ Features](#features)
- [🏗️ Engineering Highlights](#️-engineering-highlights)
- [🧠 Design Decisions](#design-decisions)
- [🛠️ Technology Stack](#technology-stack)
- [🏛️ Project Architecture](#project-architecture)
- [📂 Repository Structure](#repository-structure)
- [📚 Project Documentation](#-project-documentation)
- [📸 Application Preview](#application-preview)
- [📈 Model Performance](#model-performance)
- [📦 Dataset](#dataset)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [🔮 Future Improvements](#future-improvements)
- [🙏 Acknowledgements](#acknowledgements)
- [👨‍💻 Author](#author)
- [📄 License](#license)



# Overview

Banalyzer is a deep learning application for banana ripeness classification built using TensorFlow and MobileNetV2.

The model leverages **Transfer Learning** with **MobileNetV2**, enabling efficient image classification while maintaining a lightweight architecture suitable for real-world deployment.

The application is designed with software engineering best practices in mind, including modular architecture, reusable components, centralized configuration, structured logging, and a clean separation between training, evaluation, inference, and presentation layers.

The repository demonstrates how machine learning and software engineering practices can be combined to build a maintainable and deployable AI application.

# Why Banalyzer?

Many machine learning projects stop after training a model. Banalyzer was built to demonstrate the complete lifecycle of a production-inspired AI application.

The project combines computer vision, transfer learning, software engineering, and user-centric design into a maintainable and deployable solution. Rather than focusing solely on model accuracy, it emphasizes clean architecture, reusable components, centralized configuration, structured documentation, and an intuitive user experience.

Banalyzer reflects the engineering practices used to transform a trained model into software that can be shared, maintained, and extended.


# Features

-  Upload banana images (JPG / PNG)
-  MobileNetV2-based image classification
-  Predicts four ripeness stages:
  - Unripe
  - Ripe
  - Overripe
  - Rotten
-  Confidence gauge
-  Probability distribution
-  Prediction explanation
-  Ripeness insights
-  Prediction metadata
-  Interactive Streamlit dashboard
-  Production-ready project structure


# Engineering Highlights

- Modular software architecture
- MobileNetV2 transfer learning pipeline
- Image validation before inference
- Reusable prediction pipeline
- Centralized configuration management
- Interactive Streamlit dashboard
- Comprehensive technical documentation
- Production-inspired project organization


# Design Decisions

Banalyzer was designed as more than a machine learning experiment. This project was designed to an application that follows software engineering principles while demonstrating a complete end-to-end AI workflow.

### MobileNetV2

MobileNetV2 was selected for its balance of inference speed, computational efficiency, and classification performance, making it well suited for lightweight image classification tasks. Its lightweight design makes it suitable for real-world deployment without requiring high-end hardware.

### Transfer Learning

Training a deep neural network from scratch requires a significantly larger dataset and computational resources. Transfer Learning enables the model to leverage rich visual features learned from ImageNet while adapting efficiently to banana ripeness classification.

### Streamlit

Streamlit enables rapid deployment of machine learning applications through an intuitive web interface. It allows users to interact with the trained model without requiring knowledge of Python or machine learning workflows.

### Modular Architecture

The project separates responsibilities into dedicated modules for configuration, training, prediction, evaluation, and presentation. This improves maintainability, readability, scalability, and makes future enhancements easier to implement.

## Production-Oriented Design

The repository follows several software engineering best practices, including:

- Centralized configuration management
- Modular project structure
- Reusable prediction pipeline
- Structured logging
- Type hints
- Separation of concerns
- Production-style folder organization


# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.13 |
| Deep Learning | TensorFlow 2.20 |
| Model | MobileNetV2 |
| Computer Vision | OpenCV, Pillow |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |
| Model Format | `.keras` |


# Project Architecture

```text
                   User Upload
                        │
                        ▼
             Image Validation
                        │
                        ▼
            Image Preprocessing
                        │
                        ▼
        MobileNetV2 Deep Learning Model
                        │
                        ▼
              Prediction Engine
                        │
                        ▼
          Confidence Calculation
                        │
                        ▼
        Probability Distribution
                        │
                        ▼
      Ripeness Insights & Recommendation
                        │
                        ▼
          Interactive Streamlit UI
```


# Repository Structure

```text
Banalyzer/
│
├── assets/                 # Images and UI assets
├── data/                   # Dataset (download separately, see Dataset section)
├── docs/                   # Project documentation
├── models/                 # Trained model and class mapping
├── outputs/                # Evaluation artifacts (generated locally)
├── utils/                  # Reusable utility modules
│
├── app.py                  # Streamlit application
├── train.py                # Model training pipeline
├── evaluate.py             # Model evaluation
├── predict.py              # Prediction engine
├── config.py               # Centralized configuration
│
├── requirements.txt
├── LICENSE
└── README.md
```

# Project Documentation

Additional technical documentation is available in the `docs/` directory.

| Document | Description |
|----------|-------------|
| architecture.md | Project architecture and design decisions |
| dataset.md | Dataset organization and preprocessing |
| model.md | Model training methodology and configuration |
| deployment.md | Deployment instructions |
| testing/manual_test_matrix.md | Manual testing scenarios |
| testing/validation_summary.md | Validation results |
| testing/known_limitations.md | Current limitations and future improvements |


# Application Preview

## Home Dashboard

The application starts with a clean dashboard that presents the project overview, supported classes, model information, and image upload interface.

<p align="center">
  <img src="assets/screenshots/01-home.png" width="100%">
</p>

---

## Upload & Prediction

Users can upload a banana image and run inference directly from the web interface.

<p align="center">
  <img src="assets/screenshots/02-upload.png" width="100%">
</p>

---

## Prediction Result

The prediction panel displays the detected ripeness stage together with the confidence score.

<p align="center">
  <img src="assets/screenshots/03-prediction.png" width="100%">
</p>

---

## Confidence Analysis

Probability distribution and confidence visualization help users understand how certain the model is.

<p align="center">
  <img src="assets/screenshots/04-confidence.png" width="100%">
</p>

---

## Ripeness Insights

Beyond classification, Banalyzer provides practical recommendations based on the predicted ripeness stage.

<p align="center">
  <img src="assets/screenshots/05-insights.png" width="100%">
</p>

---

## Model Performance Dashboard

Displays inference metadata together with model specifications.

<p align="center">
  <img src="assets/screenshots/06-performance.png" width="100%">
</p>


# Model Performance

## Test Results

  Metric | Value 
------------------
  Model - MobileNetV2 
  Test Accuracy - **72.5%** 
  Number of Classes - **4** 
  Input Resolution - **224 × 224** 
  Framework - TensorFlow 2.20
  Deployment - Streamlit

---

## Training History

The following graph illustrates the evolution of training and validation accuracy/loss throughout the training process.

<p align="center">
  <img src="assets/screenshots/training-history.png" width="100%">
</p>

---

## Confusion Matrix

The confusion matrix summarizes the model's performance across all four ripeness classes and highlights common misclassifications.

<p align="center">
  <img src="assets/screenshots/confusion-matrix.png" width="70%">
</p>


### Key Observations

- The model performs best on the **Ripe** and **Rotten** classes.
- Some confusion exists between **Unripe** and **Ripe**, reflecting the visual similarity during transitional ripeness stages.
- The confusion matrix indicates that the model captures meaningful visual features while still leaving room for improvement through additional data, augmentation, or fine-tuning.


# Installation

Follow the steps below to run Banalyzer locally.

## 1. Clone the Repository

```bash
git clone https://github.com/Shivv-Dev/Banalyzer.git
cd Banalyzer
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Launch the Application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```
http://localhost:8501
```

# Usage

Using Banalyzer is straightforward:

1. Launch the Streamlit application.
2. Upload a banana image in **JPG** or **PNG** format.
3. Click **Predict Ripeness**.
4. Review the prediction dashboard.


The application provides:

- Predicted ripeness stage
- Confidence score
- Probability distribution
- Prediction explanation
- Ripeness insights
- Inference metadata
- Model performance summary


# Future Improvements 

Planned enhancements include:

- [ ] Grad-CAM visualization for explainable AI
- [ ] Batch image prediction
- [ ] Real-time webcam inference
- [ ] REST API using FastAPI
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions
- [ ] Automated model retraining pipeline
- [ ] Cloud deployment
- [ ] Model versioning
- [ ] Performance benchmarking across architectures


# Acknowledgements

This project builds upon several excellent open-source technologies:

- TensorFlow
- Streamlit
- OpenCV
- Pillow
- NumPy
- Matplotlib
- Scikit-learn

Their tools made this project possible.


# Author

**Shiva Poojith Alli**

Machine Learning | Computer Vision | Python | Software Engineering

LinkedIn: [Shiva Poojith Alli](https://www.linkedin.com/in/shiva-poojith-alli)

GitHub: [Shivv-Dev](https://github.com/Shivv-Dev)

If you found this project interesting, feel free to connect or reach out.


# License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.


---

If you found this project interesting, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.

Built with ❤️ using Python, TensorFlow, and Streamlit.
