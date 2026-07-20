# 🧠 Model Documentation

## Overview

Banalyzer uses **MobileNetV2**, a lightweight convolutional neural network pre-trained on the ImageNet dataset, as the backbone for banana ripeness classification.

The model is fine-tuned using Transfer Learning to classify banana images into four ripeness stages.

---

# 🎯 Why MobileNetV2?

Several CNN architectures were considered before selecting MobileNetV2.

The primary reasons include:

- Lightweight architecture
- Fast inference
- Strong transfer learning performance
- Lower computational requirements
- Suitable for deployment on consumer hardware

These characteristics make MobileNetV2 an excellent choice for real-time image classification applications.

---

# 🔄 Transfer Learning Strategy

Instead of training a deep neural network from scratch, Banalyzer uses Transfer Learning.

This approach enables the model to reuse rich visual representations learned from millions of ImageNet images while adapting to the banana ripeness dataset.

Benefits include:

- Reduced training time
- Better generalization
- Lower computational cost
- Improved performance on smaller datasets

---

# ⚙️ Training Configuration

| Parameter | Value |
|-----------|------:|
| Architecture | MobileNetV2 |
| Framework | TensorFlow 2.20 |
| Input Size | 224 × 224 |
| Classes | 4 |
| Output Activation | Softmax |

---

# 🍌 Target Classes

The model predicts one of four ripeness stages:

- Unripe
- Ripe
- Overripe
- Rotten

---

# 📊 Evaluation

Model performance was evaluated using a held-out test dataset.

Evaluation includes:

- Test Accuracy
- Confusion Matrix
- Class Probabilities
- Confidence Scores

The final model achieved an overall test accuracy of **72.5%**.

---

# ⚠️ Current Limitations

The model may struggle with:

- Poor lighting conditions
- Motion blur
- Occluded bananas
- Background clutter
- Transitional ripeness stages

These limitations are common in image classification systems and can be improved with additional data and further fine-tuning.

---

# 🚀 Future Improvements

Potential enhancements include:

- EfficientNet comparison
- ConvNeXt benchmarking
- Grad-CAM explainability
- Hyperparameter optimization
- Ensemble learning
- Model quantization
- ONNX export