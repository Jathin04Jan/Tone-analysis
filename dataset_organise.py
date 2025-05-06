import os
import shutil

SOURCE_DIR = "Audio_Song_Actors_01-24"
DEST_DIR = "data"

# Map emotion codes to folder names
emotion_map = {
    "03": "happy",
    "04": "sad",
    "05": "angry"
}

# Make folders
for emotion in emotion_map.values():
    os.makedirs(os.path.join(DEST_DIR, emotion), exist_ok=True)

# Move files based on emotion code (3rd segment in filename)
for actor in os.listdir(SOURCE_DIR):
    actor_dir = os.path.join(SOURCE_DIR, actor)
    if not os.path.isdir(actor_dir):
        continue  # ← Skip anything that's not a folder (e.g., .DS_Store)

    for file in os.listdir(actor_dir):
        if file.endswith(".wav"):
            parts = file.split("-")
            if len(parts) >= 3:
                emotion_code = parts[2]
                if emotion_code in emotion_map:
                    emotion_folder = emotion_map[emotion_code]
                    src = os.path.join(actor_dir, file)
                    dst = os.path.join(DEST_DIR, emotion_folder, file)
                    shutil.copyfile(src, dst)

print("✅ Audio files organized into happy, sad, and angry.")