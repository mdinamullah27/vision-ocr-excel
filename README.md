Project Structure
vision-ocr-excel/
├── app/
│   ├── main.py
│   ├── api/v1/routes/extract.py
│   ├── core/config.py
│   ├── core/openai_client.py
│   ├── services/pdf_service.py
│   ├── services/vision_service.py
│   ├── services/excel_service.py
│   ├── utils/dedup.py
│   └── utils/json_utils.py
├── temp/uploads/
├── temp/images/
├── temp/outputs/
├── .env
├── requirements.txt
└── README.md

Installation

Clone the repo:

git clone <repo_url>
cd vision-ocr-excel


Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Install system dependencies:

sudo apt install tesseract-ocr tesseract-ocr-ben poppler-utils


Add your OpenAI API key in .env:

OPENAI_API_KEY=sk-xxxxxx

Usage

Start the FastAPI server:

uvicorn app.main:app --reload# vision-ocr-excel
