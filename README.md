# 🚀 Military Vehicle Detector

A deep learning-based image classification system for detecting military vehicles using **EfficientNet-B0** architecture.  
The application provides an easy-to-use GUI for real-time classification of five different military vehicle categories.

---

## 📋 Features

- 🤖 **Deep Learning Classification**  
  Uses EfficientNet-B0 pretrained on ImageNet and fine-tuned for military vehicle recognition.

- 🖥️ **Interactive GUI**  
  Built with Tkinter for simple image selection and prediction visualization.

- ⚡ **GPU Support**  
  Automatically detects and uses CUDA-compatible GPUs for faster inference.

- 🎯 **Multi-Class Classification**  
  Classifies images into five military vehicle categories.

- ⏱️ **Real-Time Prediction**  
  Provides instant predictions with confidence-based results.

---

# 🎯 Classification Categories

The model recognizes the following military vehicles:

| Class ID | Vehicle Type |
|----------|--------------|
| 0 | Half-track |
| 1 | Helicopter |
| 2 | Jeep / Car |
| 3 | Tank |
| 4 | Warplane |

---

# 🚀 Installation

## Prerequisites

- Python 3.8+
- pip package manager
- CUDA-compatible GPU (optional)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Tariq-Zeyad/Military-Object-Detector.git

cd Military-Object-Detector
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install torch torchvision pillow
```

> Note: Tkinter is included by default with most Python installations.

---

### 4. Prepare the model

Place the trained model file:

```
best_model.pth
```

inside the project root directory.

The model must be compatible with the EfficientNet-B0 architecture.

---

# 📁 Project Structure

```
Military-Object-Detector/
│
├── main.py              # Application entry point
├── model.py             # Neural network model
├── ui.py                # Tkinter GUI interface
├── config.py            # Configuration settings
├── best_model.pth       # Trained model weights
└── README.md            # Documentation
```

---

# 🎮 Usage

Run the application:

```bash
python app.py
```

---

## Using the GUI

1. Click **"Open Image"**.
2. Select an image file.
3. The system processes the image.
4. The predicted military vehicle category appears below the image.

Supported formats:

- JPG
- JPEG
- PNG

---

# 🔧 Configuration

The `config.py` file contains adjustable parameters:

```python
CLASS_NAMES = {
    0: "half_track",
    1: "helicopter",
    2: "jeep_car",
    3: "tank",
    4: "warplane"
}

MODEL_PATH = "best_model.pth"

IMAGE_SIZE = 224
```

---

# 🏗️ Technical Architecture

## Model Architecture

**Base Model:**
- EfficientNet-B0

**Classifier Head:**

```
Dropout (0.3)
        ↓
Linear Layer
```

**Input Size:**

```
224 × 224 pixels
```

**Normalization:**

ImageNet normalization:

```python
mean = [0.485, 0.456, 0.406]

std = [0.229, 0.224, 0.225]
```

---

# 🔄 Processing Pipeline

1. Load image using PIL
2. Convert image to RGB format
3. Resize image to 224×224
4. Convert image to tensor
5. Apply ImageNet normalization
6. Run inference using CPU/GPU
7. Extract highest probability class

---

# 📊 Performance Optimization

- ✅ Single-image inference optimized for real-time prediction
- ✅ Efficient tensor operations using `torch.no_grad()`
- ✅ Automatic CPU/GPU device selection
- ✅ Memory-efficient image handling with PIL

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit changes:

```bash
git commit -m "Add some AmazingFeature"
```

4. Push your branch:

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgments

- EfficientNet architecture by Google Research
- PyTorch deep learning framework
- Tkinter GUI framework

---

# 📧 Contact

**Tariq Zeyad**

Email:
```
tariqkashan0@gmail.com
```

GitHub:
```
https://github.com/Tariq-Zeyad
```

Project Repository:

```
https://github.com/Tariq-Zeyad/Military-Object-Detector
```
