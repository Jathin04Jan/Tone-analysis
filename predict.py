from pyAudioAnalysis import audioTrainTest as aT
import sys
import os

# === CONFIG ===
MODEL_PATH = "saved_model/emotion_model"
CLASSIFIER_TYPE = "svm"

def predict_emotion(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    res, _, class_names = aT.file_classification(file_path, MODEL_PATH, CLASSIFIER_TYPE)
    predicted_label = class_names[int(res)]
    
    print(f"\n🎤 Predicted Emotion: **{predicted_label.upper()}**")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py path_to_audio.wav")
    else:
        predict_emotion(sys.argv[1])
        