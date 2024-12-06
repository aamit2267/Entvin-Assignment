import os
import logging
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from utils import extract_text_from_pdf
from diff_generator import generate_diff_pdf

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/compare-pdfs/", response_description="Download the difference PDF")
async def compare_pdfs(old_file: UploadFile, new_file: UploadFile):
    try:
        old_path = os.path.join(UPLOAD_DIR, old_file.filename)
        new_path = os.path.join(UPLOAD_DIR, new_file.filename)
        
        with open(old_path, "wb") as old_f:
            old_f.write(await old_file.read())
        
        with open(new_path, "wb") as new_f:
            new_f.write(await new_file.read())
        
        old_text = extract_text_from_pdf(old_path).replace("  ", " ").strip()
        new_text = extract_text_from_pdf(new_path).replace("  ", " ").strip()
        
        output_pdf_path = generate_diff_pdf(old_text, new_text, OUTPUT_DIR)
        
        if not os.path.exists(output_pdf_path):
            raise FileNotFoundError(f"Output PDF not found: {output_pdf_path}")
        
        return FileResponse(output_pdf_path, media_type="application/pdf", filename="diff_output.pdf")
    
    except Exception as e:
        logger.error(f"Error during comparison: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")