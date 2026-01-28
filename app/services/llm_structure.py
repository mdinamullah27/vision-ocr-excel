from app.core.openai_client import client
from app.utils.json_utils import extract_json

def structure_voter(text_block: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": (
                "Convert Bangla voter text into JSON.\n"
                "Return ONE object only.\n"
                "Fields: name, voter_no, father, mother, dob, address."
            )},
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


