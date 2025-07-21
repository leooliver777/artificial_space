# pdf_utils.py
import fitz  # PyMuPDF

def extract_pdf_content(file_path):
    """
    Extracts text content from each page of the given PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        list: A list of dictionaries with 'page' number and 'text' content.
    """
    doc = fitz.open(file_path)
    content = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        content.append({
            "page": page_num + 1,
            "text": text.strip()
        })
    return content
