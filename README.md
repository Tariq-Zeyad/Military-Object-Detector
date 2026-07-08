# 🚀 AI-Detections - Military Vehicle Detector

A deep learning-based image classification system for detecting military vehicles using **EfficientNet-B0** architecture.

The project includes a trained deep learning model, a graphical user interface (GUI), and a complete training notebook for building and fine-tuning the model.

The application can classify military vehicle images into five different categories in real time.

---

# 📋 Features

- 🤖 **Deep Learning Classification**
  
  Uses **EfficientNet-B0** pretrained on ImageNet and fine-tuned for military vehicle recognition.

- 🖥️ **Interactive GUI**

  A user-friendly interface built with Tkinter for selecting images and displaying prediction results.

- ⚡ **GPU Support**

  Automatically detects CUDA-compatible GPUs for faster model inference.

- 🎯 **Multi-Class Classification**

  Recognizes five different military vehicle categories.

- ⏱️ **Real-Time Prediction**

  Provides instant classification results.

- 📚 **Training Notebook Included**

  The complete model training process is available in:

```
Model/Military__Vehicle__Detector.ipynb
```

---

# 🎯 Classification Categories

The model recognizes:

| Class ID | Vehicle Type |
|----------|--------------|
| 0 | Half-track |
| 1 | Helicopter |
| 2 | Jeep / Car |
| 3 | Tank |
| 4 | Warplane |

---

# 🚀 Installation

## Requirements

- Python 3.8+
- pip package manager
- CUDA-compatible GPU (optional)

---

# ⚙️ Setup

## 1. Clone Repository

```bash
git clone https://github.com/Tariq-Zeyad/Military-Object-Detector.git

cd Ai-Detections
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install torch torchvision pillow
```

---

# 📁 Project Structure

```
Ai-Detections/
│
├── app.py                         # Application entry point
├── model.py                        # Neural network architecture
├── ui.py                           # Tkinter GUI
├── config.py                       # Configuration parameters
│
├── Model/
│   ├── Military__Vehicle__Detector.ipynb
│── best_model.pth              # Trained model weights
│
└── README.md
```

---

# 🧠 Model Training

The training process was performed using Jupyter Notebook:

```
Model/Military__Vehicle__Detector.ipynb
```

The notebook includes:

- Dataset preparation
- Image preprocessing
- Data augmentation
- EfficientNet-B0 fine-tuning
- Model evaluation
- Saving the best model

The final trained model is saved as:

```
best_model.pth
```

---

# 🎮 Usage

Run the application:

```bash
python main.py
```

---

## Using the GUI

1. Click **Open Image**.
2. Select an image.
3. The system processes the image.
4. The predicted military vehicle category is displayed.

Supported formats:

- JPG
- JPEG
- PNG

---

# 🔧 Configuration

The model classes and settings are defined in:

```
config.py
```

Example:

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

## Model

**Architecture:**

```
EfficientNet-B0
```

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

```python
mean = [0.485, 0.456, 0.406]

std = [0.229, 0.224, 0.225]
```

---

# 🔄 Inference Pipeline

1. Load image using PIL.
2. Convert image to RGB.
3. Resize image to 224×224.
4. Convert image into Tensor.
5. Apply ImageNet normalization.
6. Run inference using CPU/GPU.
7. Return the predicted class.

---

# 📊 Performance Optimization

- ✅ Optimized single-image inference.
- ✅ Uses `torch.no_grad()` for efficient prediction.
- ✅ Automatic CPU/GPU selection.
- ✅ Memory-efficient image processing.

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/NewFeature
```

3. Commit changes:

```bash
git commit -m "Add new feature"
```

4. Push changes:

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgments

- EfficientNet architecture by Google Research.
- PyTorch deep learning framework.
- Tkinter GUI framework.

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
