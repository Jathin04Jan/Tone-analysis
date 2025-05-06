from pyAudioAnalysis import audioTrainTest as aT

# Folder paths — make sure these folders exist and have .wav files in them
emotion_dirs = ["data/happy", "data/sad", "data/angry"]

# Train using all data and save model
aT.extract_features_and_train(
    emotion_dirs,
    1.0, 1.0,       # mid-term
    0.05, 0.05,     # short-term
    "svm",          # classifier
    "emotion_model",# base name for model files
    False           # no beat features
)