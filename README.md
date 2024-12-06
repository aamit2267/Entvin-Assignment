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

## Known Limitations

1. **Formatting Issues**:
   - The tool only extracts plain text from PDFs, and formatting such as bold, italics, or tables is not retained.
   - PDF files with complex layouts, such as multi-column text or heavy use of images, may not be processed accurately.

2. **Text Alignment**:
   - Differences are displayed in a linear manner. Overlapping text or alignment issues may arise for PDFs with irregular text flow.

3. **Unsupported Characters**:
   - Non-standard or unsupported character encodings in the PDF may lead to inaccurate text extraction or comparison.

4. **Performance**:
   - Comparing large PDFs with many pages may result in slower processing times.

5. **Highlighting**:
   - The tool highlights differences in a basic manner. It does not provide advanced diff visualization for word-level changes in continuous lines.

6. **File Type**:
   - Currently supports only PDF files. Other file formats (e.g., Word, Excel) are not supported.

7. **Graphical Content**:
   - This tool does not compare graphical content, charts, or images in PDFs.

8. **Whitespace Handling**:
   - Excessive or missing whitespaces may affect the diff results as they are treated as differences.

Feel free to contribute or suggest improvements to address these limitations!

---

## Dependencies

- **FastAPI**: Framework for building APIs.
- **PyMuPDF**: Extracts text from PDF files.
- **ReportLab**: Generates the difference PDF.

--- 

Feel free to customize and extend this tool to fit your needs!