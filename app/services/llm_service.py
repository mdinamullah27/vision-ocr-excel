from app.core.openai_client import client
import re
import json

def extract_json(text: str):
    """Safely parse JSON from LLM output"""
    if not text:
        raise ValueError("Empty response from model")

    text = re.sub(r"```json|```", "", text, flags=re.IGNORECASE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"(\[.*\]|\{.*\})", text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
    raise ValueError("No valid JSON found")

def structure_voter(text_block: str):
    """Call LLM to convert voter text to JSON"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Convert Bangla voter text into JSON.\n"
                    "Return ONE object only.\n"
                    "Fields: name, voter_no, father, mother, dob, address."
                )
            },
            {"role": "user", "content": text_block}
        ],
        temperature=0
    )

    data = extract_json(response.choices[0].message.content)

    if isinstance(data, list) and len(data) > 0:
        data = data[0]
    elif not isinstance(data, dict):
        data = {}

    # Ensure all fields exist
    for f in ["name", "voter_no", "father", "mother", "dob", "address"]:
        data.setdefault(f, "")

    return data
