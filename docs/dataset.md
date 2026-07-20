# 📂 Dataset Documentation

## Overview

The Banalyzer dataset consists of labeled banana images grouped into four ripeness stages.

The dataset is organized into dedicated training and testing directories to ensure consistent evaluation.

---

# 🍌 Classes

The dataset contains the following categories:

- Unripe
- Ripe
- Overripe
- Rotten

---

# 📁 Directory Structure

```text
data/
│
├── train/
│   ├── unripe/
│   ├── ripe/
│   ├── overripe/
│   └── rotten/
│
└── test/
    ├── unripe/
    ├── ripe/
    ├── overripe/
    └── rotten/
```

---

# 🧹 Preprocessing

Before training, every image is:

- Resized to 224 × 224 pixels
- Converted to RGB
- Normalized
- Converted into tensors

These preprocessing steps ensure compatibility with MobileNetV2.

---

# 🔄 Data Augmentation

To improve generalization, augmentation techniques may include:

- Random Rotation
- Horizontal Flip
- Zoom
- Brightness Adjustment

These augmentations increase dataset diversity and help reduce overfitting.

---

# 📊 Dataset Split

The dataset is divided into:

- Training Set
- Test Set

The test dataset is used exclusively for evaluating model performance.

---

# ⚠️ Dataset Challenges

Several factors make banana ripeness classification difficult:

- Similar appearance between adjacent ripeness stages
- Lighting variation
- Background variation
- Image quality differences

These challenges contribute to real-world prediction complexity.

---

# 🚀 Future Improvements

Future dataset enhancements may include:

- Larger dataset
- More balanced class distribution
- Additional lighting conditions
- Multiple banana varieties
- Synthetic augmentation