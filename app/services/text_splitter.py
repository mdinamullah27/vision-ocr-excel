import re

def split_voters(text: str):
    blocks = re.split(r"\n\s*\d+\.\s*", text)
    # Keep everything, strip only
    return [b.strip() for b in blocks if b.strip()]

