import os
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT

def cross_validation_wrapper(directories, mt_win, mt_step, st_win, classifier_type):
    accuracies = []

    for i in range(10):  # 10-fold cross-validation
        print(f"\nFold {i + 1}/10")

        # Create train/test splits
        for d in directories:
            files = os.listdir(d)
            files = [f for f in files if f.endswith(".wav")]
            np.random.shuffle(files)
            N = len(files)
            split_point = int(0.9 * N)
            train_files = files[:split_point]
            test_files = files[split_point:]

            os.makedirs(f"temp_train/{os.path.basename(d)}", exist_ok=True)
            os.makedirs(f"temp_test/{os.path.basename(d)}", exist_ok=True)

            for f in train_files:
                os.system(f"cp '{d}/{f}' 'temp_train/{os.path.basename(d)}/{f}'")
            for f in test_files:
                os.system(f"cp '{d}/{f}' 'temp_test/{os.path.basename(d)}/{f}'")

        # Train the model on training set
        train_dirs = [f"temp_train/{os.path.basename(d)}" for d in directories]
        aT.extract_features_and_train(
            train_dirs,
            mt_win, mt_step,
            st_win, st_win,
            classifier_type, "temp_model", False
        )

        # Test the model on test set
        correct, total = 0, 0
        for d in directories:
            label = os.path.basename(d)
            test_path = f"temp_test/{label}"

            for f in os.listdir(test_path):
                if f.endswith(".wav"):
                    filepath = os.path.join(test_path, f)
                    res, _, classNames = aT.file_classification(filepath, "temp_model", classifier_type)
                    pred = classNames[int(res)]
                    if pred == label:
                        correct += 1
                    total += 1

        acc = correct / total if total else 0
        print(f"→ Accuracy: {acc:.2f}")
        accuracies.append(acc)

        # Cleanup temp data
        os.system("rm -rf temp_train temp_test temp_model")

    print("\n✅ Final Evaluation")
    print(f"Mean Accuracy: {np.mean(accuracies):.4f}")
    print(f"Standard Deviation: {np.std(accuracies):.4f}")

# Your labeled dataset folders
emotion_dirs = ["data/happy", "data/sad", "data/angry"]

# ✅ Call with proper short-term window size (e.g., 0.05 sec)
cross_validation_wrapper(emotion_dirs, 1.0, 1.0, 0.05, "svm")