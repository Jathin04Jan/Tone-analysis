# 🎤 Voice Tone Classification using pyAudioAnalysis

This project is a simple yet powerful proof-of-concept (PoC) for classifying human voice tones such as **Happy**, **Sad**, and **Angry** from `.wav` audio files using machine learning (SVM) and the open-source `pyAudioAnalysis` library.

---

## 📁 Project Structure

```
Tone-analysis/
├── data/
│   ├── happy/         # Labeled .wav files for "happy"
│   ├── sad/           # Labeled .wav files for "sad"
│   └── angry/         # Labeled .wav files for "angry"
├── saved_model/
│   ├── emotion_model            # Trained SVM model
│   ├── emotion_modelMEANS       # Feature normalization info
│   └── emotion_modelClasses     # Label mapping file
├── evaluate_model.py     # Performs 10-fold cross-validation
├── train_model.py        # Trains model on full dataset
├── predict.py            # Classifies a given .wav file
├── requirements.txt
└── README.md
```

---

## 🧠 Features

- Classifies voice tone as **Happy**, **Sad**, or **Angry**
- Uses `pyAudioAnalysis` for feature extraction and training
- Built-in model saving and reusability
- Includes model evaluation (10-fold CV)
- Command-line interface for single audio prediction

---

## 🚀 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tone-analysis.git
cd tone-analysis
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python3 -m venv audioEnv
source audioEnv/bin/activate
```

### 3. Install Required Dependencies

Install all Python packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (Required by pyAudioAnalysis)

#### On macOS (using Homebrew):

```bash
brew install ffmpeg
```

#### On Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

---

## 🎓 Dataset Preparation

Create a folder named `data/` and place your labeled `.wav` files in these subfolders:

```
data/
├── happy/
├── sad/
└── angry/
```

Each subfolder must contain `.wav` files representing that emotion.  
Make sure all files are mono/stereo `.wav` and reasonably clean.

---

## 📊 Model Evaluation (Cross-Validation)

To evaluate model performance using 10-fold cross-validation:

```bash
python evaluate_model.py
```

Expected output:

```
Fold 1/10 → Accuracy: 0.88
...
✅ Final Evaluation
Mean Accuracy: 0.8422
Standard Deviation: 0.0452
```

---

## 🧠 Model Training

Train the model on **all available data** and save it for later predictions:

```bash
python train_model.py
```

This will generate:

```
saved_model/
├── emotion_model
├── emotion_modelMEANS
└── emotion_modelClasses
```

---

## 🔍 Making Predictions

To predict the tone of a given `.wav` file using the saved model:

### Usage:

```bash
python predict.py path/to/your_audio.wav
```

### Example:

```bash
python predict.py test_samples/angry_example.wav
```

Expected output:

```
🎤 Predicted Emotion: **ANGRY**
```

---

## 🔧 Notes

- Audio files must be in `.wav` format.
- Recommended audio length: **2–6 seconds** for better feature extraction.
- If you see warnings like `WavFileWarning: Chunk (non-data) not understood`, you can ignore them — they’re safe.

---

## 🧼 Optional Cleanup

After running evaluation or training, you may delete intermediate files like:

```bash
rm -rf temp_model* temp_train/ temp_test/
```

---

## 👨‍💻 Author

- **Jathin Narayan** — Developer and ML enthusiast  
- Feel free to fork, contribute, or star ⭐️ this project!

---

## 📜 License

This project is open-sourced under the MIT License. Feel free to use and modify it for your own tone classification projects.

---

## 🙋‍♂️ Need Help?

DM me on [LinkedIn](https://www.linkedin.com/) or open an issue here if you're facing any problems getting started.