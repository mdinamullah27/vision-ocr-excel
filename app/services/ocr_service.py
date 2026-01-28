import easyocr

reader = easyocr.Reader(['bn', 'en'])

def ocr_image(image_path: str) -> str:
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)
