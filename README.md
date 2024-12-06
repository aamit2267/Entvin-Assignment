# PDF Comparison Tool

Welcome to the **PDF Comparison Tool**, a simple and efficient solution to compare two PDF files for text differences. This tool extracts text from two PDF files, identifies the differences, and generates a new PDF highlighting the changes.

---

## Features

- Extracts and compares text from two PDF files.
- Highlights **deleted text** in **red** and **added text** in **green**.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aamit2267/Entvin-Assignment.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Entvin-Assignment
   ```
3. Install dependencies:
- For Windows
   ```bash
   pip install -r requirements.txt
   ```
- For Windows
   ```bash
   pip3 install -r requirements.txt
   ```

---

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:8000/docs
   ```
3. Upload two PDF files (`old_file` and `new_file`) through the provided interface (Swagger UI).
4. Download the generated PDF with differences.

---

## Sample Files

- [Old File](https://github.com/aamit2267/Entvin-Assignment/blob/main/uploads/oldPDF.pdf) (Sample input for testing)
- [New File](https://github.com/aamit2267/Entvin-Assignment/blob/main/uploads/latestPDF.pdf) (Sample input for testing)
- [Output File](https://github.com/aamit2267/Entvin-Assignment/blob/main/output/diff_output.pdf) (Sample output with differences)

---

## Project Structure

- `main.py`: Entry point for the FastAPI application.
- `diff_generator.py`: Contains logic for generating the difference PDF.
- `utils.py`: Utility functions for text extraction from PDF files using PyMuPDF.

---

## Dependencies

- **FastAPI**: Framework for building APIs.
- **PyMuPDF**: Extracts text from PDF files.
- **ReportLab**: Generates the difference PDF.

--- 

Feel free to customize and extend this tool to fit your needs!