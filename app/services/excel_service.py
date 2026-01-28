import os, uuid
import pandas as pd

OUTPUT_DIR = "temp/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_excel(voters):
    filename = f"voters_{uuid.uuid4().hex}.xlsx"
    path = os.path.join(OUTPUT_DIR, filename)
    df = pd.DataFrame(voters)
    df.to_excel(path, index=False)
    return path
