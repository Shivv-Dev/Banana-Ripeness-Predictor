# Section 1:🍌 Banalyzer

# AI-Powered Banana Ripeness Classification using Deep Learning

> **From image to insight, one banana at a time.**

Banalyzer is a production-inspired computer vision application that predicts the ripeness stage of a banana from a single image using **TensorFlow**, **MobileNetV2 Transfer Learning**, and **Streamlit**.

The project demonstrates an end-to-end machine learning workflow, including data preprocessing, model training, evaluation, inference, and deployment through an interactive web application.

---

# Section 2: Highlights

- 🍌 Classifies bananas into **4 ripeness stages**
- 🧠 MobileNetV2 Transfer Learning
- 📊 Interactive confidence analysis
- 📈 Probability distribution visualization
- 💡 Ripeness insights & recommendations
- ⚡ Streamlit-powered web application
- 🏗️ Modular production-style architecture

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-FF6F00?style=for-the-badge&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![MobileNetV2](https://img.shields.io/badge/Model-MobileNetV2-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)


# Section 3: Project Overview

Banalyzer is an image classification application that predicts the ripeness stage of bananas using deep learning.

The model leverages **Transfer Learning** with **MobileNetV2**, enabling efficient image classification while maintaining a lightweight architecture suitable for real-world deployment.

The application is designed with software engineering best practices in mind, including modular architecture, reusable components, centralized configuration, structured logging, and a clean separation between training, evaluation, inference, and presentation layers.

This repository showcases not only machine learning techniques but also the engineering practices required to build production-ready AI applications.


# Section 4: Features

- 📸 Upload banana images (JPG / PNG)
- 🧠 MobileNetV2-based image classification
- 🍌 Predicts four ripeness stages:
  - Unripe
  - Ripe
  - Overripe
  - Rotten
- 📊 Confidence gauge
- 📈 Probability distribution
- 💡 Prediction explanation
- 🍽️ Ripeness insights
- ⏱️ Prediction metadata
- 📱 Interactive Streamlit dashboard
- 📂 Production-ready project structure


# Section 5:🧠 Engineering Highlights

Banalyzer was designed as more than a machine learning experiment. The goal was to build an application that follows software engineering principles while demonstrating a complete end-to-end AI workflow.

## Why MobileNetV2?

MobileNetV2 was selected as the backbone architecture because it provides an excellent balance between inference speed, computational efficiency, and classification accuracy. Its lightweight design makes it suitable for real-world deployment without requiring high-end hardware.

## Why Transfer Learning?

Training a deep neural network from scratch requires a significantly larger dataset and computational resources. Transfer Learning enables the model to leverage rich visual features learned from ImageNet while adapting efficiently to banana ripeness classification.

## Why Streamlit?

Streamlit enables rapid deployment of machine learning applications through an intuitive web interface. It allows users to interact with the trained model without requiring knowledge of Python or machine learning workflows.

## Why a Modular Architecture?

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


# Section 6: 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Deep Learning | TensorFlow 2.20 |
| Model | MobileNetV2 |
| Computer Vision | OpenCV, Pillow |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |
| Model Format | `.keras` |


# Section 7:🏗️ Project Architecture

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


# Section 8: 📂 Repository Structure

```text
Banalyzer/
│
├── assets/                 # Images and UI assets
├── data/                   # Training and testing datasets
├── docs/                   # Project documentation
├── logs/                   # Training and evaluation logs
├── models/                 # Trained model and class mapping
├── outputs/                # Generated evaluation results
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


# Section 9:📸 Application Preview

## 🏠 Home Dashboard

The application starts with a clean dashboard that presents the project overview, supported classes, model information, and image upload interface.

<p align="center">
  <img src="assets/screenshots/01-home.png" width="100%">
</p>

---

## 📤 Upload & Prediction

Users can upload a banana image and run inference directly from the web interface.

<p align="center">
  <img src="assets/screenshots/02-upload.png" width="100%">
</p>

---

## 🧠 Prediction Result

The prediction panel displays the detected ripeness stage together with the confidence score.

<p align="center">
  <img src="assets/screenshots/03-prediction.png" width="100%">
</p>

---

## 📊 Confidence Analysis

Probability distribution and confidence visualization help users understand how certain the model is.

<p align="center">
  <img src="assets/screenshots/04-confidence.png" width="100%">
</p>

---

## 💡 Ripeness Insights

Beyond classification, Banalyzer provides practical recommendations based on the predicted ripeness stage.

<p align="center">
  <img src="assets/screenshots/05-insights.png" width="100%">
</p>

---

## ⚡ Model Performance Dashboard

Displays inference metadata together with model specifications.

<p align="center">
  <img src="assets/screenshots/06-performance.png" width="100%">
</p>


# Section 10: 📊 Model Performance

## Test Results

| Metric | Value |
|---------|-------|
| Model | MobileNetV2 |
| Test Accuracy | **72.5%** |
| Number of Classes | **4** |
| Input Resolution | **224 × 224** |
| Framework | TensorFlow 2.20 |
| Deployment | Streamlit |

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


# Section 11:⚙️ Installation

Follow the steps below to run Banalyzer locally.

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Banalyzer.git
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

# Section 12: ▶️ Usage

Using Banalyzer is straightforward:

1. Launch the Streamlit application.
2. Upload a banana image in **JPG** or **PNG** format.
3. Click **Predict Ripeness**.
4. Review the prediction dashboard.

The application provides:

- 🍌 Predicted ripeness stage
- 📊 Confidence score
- 📈 Probability distribution
- 🧠 Prediction explanation
- 💡 Ripeness insights
- ⚡ Inference metadata
- 📱 Model performance summary


# Section 13: 🛣️  Future Improvements 

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


# Section 14: 🙏 Acknowledgements

Special thanks to the open-source community and the developers behind:

- TensorFlow
- Streamlit
- OpenCV
- Pillow
- NumPy
- Matplotlib
- Scikit-learn

Their tools made this project possible.


# 👨‍💻 Author

**Shiva Poojith Alli**

AI • Machine Learning • Computer Vision • Software Engineering

- 💼 LinkedIn: https://www.linkedin.com/in/shiva-poojith-alli
- 💻 GitHub: https://github.com/Shivv-Dev

If you found this project interesting, feel free to connect or reach out.


# 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.


---

⭐ If you found this project useful or interesting, consider giving it a star. Your support helps the project reach more developers and motivates future improvements.

Thank you for taking the time to explore Banalyzer! 🍌
























































# 🍌 Banalyzer
**A Banana Ripeness Classifier**

A deep learning project that classifies bananas into four ripeness categories: **Unripe**, **Ripe**, **Overripe**, and **Rotten** using transfer learning with MobileNetV2.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Dataset Setup](#-dataset-setup)
- [Usage](#-usage)
  - [Training the Model](#-training-the-model)
  - [Making Predictions](#-making-predictions)
  - [Running the Web App](#-running-the-web-app)
- [Model Performance](#-model-performance)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This project uses computer vision and deep learning to automatically identify the ripeness stage of bananas from images. It's useful for:

- 🏪 Food quality control in grocery stores
- 📦 Inventory management and sorting
- ♻️ Reducing food waste by optimal usage timing
- 🎓 Learning about image classification and transfer learning
- 🔬 Research in agricultural automation

---

## ✨ Features

- **🤖 Transfer Learning**: Leverages pre-trained MobileNetV2 for efficient training
- **🎯 4-Class Classification**: Accurately categorizes as Unripe, Ripe, Overripe, or Rotten
- **📊 Data Augmentation**: Improves model generalization and robustness
- **💻 Command-Line Interface**: Simple prediction script for batch processing
- **🌐 Interactive Web App**: User-friendly Streamlit interface for instant classification
- **📈 Training Visualization**: Detailed plots of training metrics
- **🚀 Production Ready**: Easy to deploy on cloud platforms

---

## 🗂️ Project Structure

```
Banalyzer/
├── src/
│   ├── train.py              # Model training script
│   └── predict.py            # Image prediction script
├── streamlitapp.py          # Streamlit web application
├── requirements.txt         # Python dependencies
├── DATASET_INFO.md          # Dataset documentation
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

**Note**: The `data/` and `models/` folders are not included in this repository due to size constraints.

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/iamchaarles/Banalyzer.git
cd Banalyzer
```

2. **Create and activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset Setup

The training dataset is not included in this repository due to size constraints. To use this project:

1. Prepare your banana images organized by ripeness category
2. Follow the structure detailed in [DATASET_INFO.md](DATASET_INFO.md)
3. Organize images in the following directory structure:

```
data/
├── train/
│   ├── unripe/
│   ├── ripe/
│   ├── overripe/
│   └── rotten/
└── test/
    ├── unripe_test/
    ├── ripe_test/
    ├── over_ripe_test/
    └── rotten_test/
```

**Dataset Sources:**
- Collect your own banana images at different ripeness stages
- Use public datasets from Kaggle or similar platforms
- Ensure balanced representation across all four categories

---

## 💡 Usage

### 🎓 Training the Model

Train your own model with your dataset:

```bash
python src/train.py
```

**This will:**
- Load and augment your dataset
- Build a MobileNetV2-based transfer learning model
- Train for up to 20 epochs (with early stopping)
- Save the best model to `models/best_model.keras`
- Generate training history plots

**Training time:** 5-15 minutes on modern CPU, 2-5 minutes with GPU

---

### 🔮 Making Predictions

Test the model on individual images using the command line:

```bash
python src/predict.py path/to/your/banana.jpg
```

**Example Output:**

```
============================================================
PREDICTION RESULTS
============================================================

Predicted Class: RIPE
Confidence: 94.32%

All Class Probabilities:
----------------------------------------
unripe      :  2.15% █
ripe        : 94.32% ███████████████████████████████████████████████
overripe    :  3.21% █
rotten      :  0.32% 

============================================================
✓ High confidence prediction
```

---

### 🌐 Running the Web App

Launch the interactive Streamlit web application:

```bash
streamlit run streamlitapp.py
```

**Features:**
- 📤 Drag-and-drop image upload
- 📸 Use your device camera
- ⚡ Real-time classification
- 📊 Confidence score visualization
- 🎨 Beautiful, responsive UI

The app will open in your browser at `http://localhost:8501`

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| **Architecture** | MobileNetV2 + Custom Head |
| **Input Size** | 640x640x3 RGB |
| **Total Parameters** | ~2.5M (trainable) |
| **Training Time** | ~10 min (CPU) / ~3 min (GPU) |
| **Validation Accuracy** | ~85-95% (dataset-dependent) |
| **Model Size** | ~15 MB |
| **Inference Time** | <100ms per image |

**Model Architecture:**
- Base: MobileNetV2 (pre-trained on ImageNet)
- Global Average Pooling
- Dropout (0.3)
- Dense Layer (128 units, ReLU)
- Dropout (0.2)
- Output Layer (4 units, Softmax)

---

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. Fork this repository
2. Create a [Streamlit Cloud](https://share.streamlit.io) account
3. Click "New app" and connect your GitHub repository
4. Select `streamlitapp.py` as the main file
5. **Important:** Upload your trained model (`best_model.keras`) to the `models/` folder before deployment

### Deploy on Hugging Face Spaces

1. Create a [Hugging Face](https://huggingface.co) account
2. Create a new Space with Streamlit template
3. Upload all project files including the trained model
4. The app will automatically deploy

### Local Deployment with Docker (Optional)

```bash
# Coming soon - Docker support
```

---

## 🔮 Future Improvements

- [ ] Increase training dataset size and diversity
- [ ] Add multi-banana detection and counting
- [ ] Implement REST API (Flask/FastAPI)
- [ ] Create mobile application (iOS/Android)
- [ ] Add nutritional information based on ripeness
- [ ] Real-time video classification
- [ ] Export to TensorFlow Lite for mobile deployment
- [ ] Add explainability features (Grad-CAM visualizations)
- [ ] Support for other fruits

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- TensorFlow and Keras teams for the amazing deep learning framework
- Google for the MobileNetV2 architecture
- Streamlit for the intuitive web app framework
- The open-source community for inspiration and support

---

## 📧 Contact

**Charles** - [@iamchaarles](https://github.com/iamchaarles)

**Project Link**: [https://github.com/iamchaarles/Banalyzer](https://github.com/iamchaarles/Banalyzer)

---

<div align="center">

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

Made with ❤️ and 🍌

</div>
