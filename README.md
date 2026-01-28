# Vision OCR to Excel

A FastAPI project to **extract Bangla voter information from PDF files** and export it to Excel. The project uses **OCR + OpenAI GPT-5** for accurate text extraction and structuring.

---

## Features

* Multi-page PDF support
* Bangla + English OCR using **Tesseract**
* GPT-5 parsing for structured voter info
* Deduplication of extracted voters
* Excel export of results
* Handles large PDFs efficiently with batching

---

## Project Structure

```
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
```

---

## Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd vision-ocr-excel
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

4. Install system dependencies:

```bash
sudo apt install tesseract-ocr tesseract-ocr-ben poppler-utils
```

5. Add your OpenAI API key in `.env`:

```
OPENAI_API_KEY=sk-xxxxxx
```

---

## Usage

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

* Open API docs: `http://127.0.0.1:8000/docs`
* Endpoint: `POST /api/v1/extract-voters` (upload a PDF)
* Returns JSON with:

  * `expected_blocks`: number of text blocks detected
  * `extracted_voters`: number of voters extracted
  * `download_url`: link to download Excel file

---

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/extract-voters" \
  -F "file=@voters.pdf"
```

Example response:

```json
{
  "expected_blocks": 50,
  "extracted_voters": 48,
  "download_url": "/api/v1/download/voters_123abc.xlsx"
}
```

---

## Notes

* Best results with **clean scanned PDFs**
* Designed specifically for **Ban
