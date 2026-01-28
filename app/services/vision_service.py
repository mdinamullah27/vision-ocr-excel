import pytesseract
import cv2
from app.core.openai_client import client
from app.utils.json_utils import extract_json
from app.utils.dedup import deduplicate

def ocr_image(image_path: str) -> str:
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    return pytesseract.image_to_string(gray, lang="ben+eng", config="--psm 6")

def split_text_blocks(text: str):
    import re
    blocks = re.split(r"\n\s*\d+\.\s*", text)
    return [b.strip() for b in blocks if len(b.strip()) > 30]

def extract_voters_from_text_blocks(blocks):
    voters = []
    batch_size = 5  # Send 5 blocks per GPT request to avoid token limit
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i+batch_size]
        prompt = (
            "Convert the following Bangla voter information into JSON array.\n"
            "Each voter should have fields: name, voter_no, father, mother, dob, address.\n"
            "Batch:\n" + "\n\n".join(batch)
        )
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are an OCR assistant for Bangla voter lists."},
                {"role": "user", "content": prompt}
            ]
        )
        voters_batch = extract_json(response.choices[0].message.content)
        if isinstance(voters_batch, dict):
            voters_batch = [voters_batch]
        voters.extend(voters_batch)
    return deduplicate(voters)
