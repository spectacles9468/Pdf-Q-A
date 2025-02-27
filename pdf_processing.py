import pymupdf
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Extracting text from pdf
def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = chr(12).join([page.get_text("text") for page in doc])
    return text

# Chunking the text for the model
def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
