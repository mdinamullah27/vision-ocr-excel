import os, uuid, shutil
from fastapi import UploadFile
from pdf2image import convert_from_path

UPLOAD_DIR = "temp/uploads"
IMAGE_DIR = "temp/images"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

def save_upload(file: UploadFile) -> str:
    path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return path

def pdf_to_images(pdf_path: str, dpi=150):
    pages = convert_from_path(pdf_path, dpi=dpi)
    image_paths = []
    for i, page in enumerate(pages):
        img_path = os.path.join(IMAGE_DIR, f"{uuid.uuid4()}_{i}.png")
        page.save(img_path, "PNG")
        image_paths.append(img_path)
    return image_paths
