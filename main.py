import pdfplumber

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

resume_text = extract_text("resume.pdf.pdf")

print("===== RESUME TEXT =====\n")
print(resume_text)