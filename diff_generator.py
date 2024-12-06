from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from difflib import unified_diff
import os

def generate_diff_pdf(old_text, new_text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "diff_output.pdf")
    
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 10)
    
    diff = unified_diff(old_text.splitlines(), new_text.splitlines())
    y_position = 750
    co = 0
    for line in diff:
        co += 1
        if co <= 2:
            continue
        if y_position < 50:
            c.showPage()
            y_position = 750

        if line.startswith('+'):
            if line[1:].isspace():
                continue
            c.setFillColor(colors.green)
        elif line.startswith('-'):
            if line[1:].isspace():
                continue
            c.setFillColor(colors.red)
        else:
            continue
        
        c.drawString(50, y_position, line)
        y_position -= 12
    
    c.save()
    return output_path
