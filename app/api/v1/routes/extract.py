from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import save_upload, pdf_to_images
from app.services.vision_service import ocr_image, split_text_blocks, extract_voters_from_text_blocks
from app.services.excel_service import create_excel

router = APIRouter(prefix="/api/v1", tags=["Voter Extraction"])

@router.post("/extract-voters")
async def extract_voters(file: UploadFile = File(...)):
    pdf_path = save_upload(file)
    images = pdf_to_images(pdf_path)

    raw_blocks = []
    for img in images:
        text = ocr_image(img)
        blocks = split_text_blocks(text)
        raw_blocks.extend(blocks)

    voters = extract_voters_from_text_blocks(raw_blocks)
    excel_path = create_excel(voters)

    return {
        "expected_blocks": len(raw_blocks),
        "extracted_voters": len(voters),
        "download_url": f"/api/v1/download/{excel_path.split('/')[-1]}"
    }
