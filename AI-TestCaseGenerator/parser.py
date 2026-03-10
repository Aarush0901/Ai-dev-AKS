from docx import Document

def extract_steps(file_path):

    doc = Document(file_path)
    steps = []

    for para in doc.paragraphs:
        text = para.text.strip()

        if text != "":
            steps.append(text)

    return steps