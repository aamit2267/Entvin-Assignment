import pymupdf

def extract_text_from_pdf(pdf_path):
    try:
        with pymupdf.open(pdf_path) as pdf:
            return chr(12).join([page.get_text() for page in pdf])
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {str(e)}")