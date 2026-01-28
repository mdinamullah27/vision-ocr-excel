import os, shutil

def save_upload(file):
    os.makedirs("temp/uploads", exist_ok=True)
    path = f"temp/uploads/{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return path
