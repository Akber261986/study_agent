from pypdf import PdfReader
from agents import function_tool

CACHE_FILE = "pdf_text_cache.txt"


def extract_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file, cache it, and return the plain text."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    cache_pdf_text(text)
    return text


def cache_pdf_text(text: str) -> str:
    """Persist the extracted PDF text so the agent can read it later."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    return "Cached PDF text."


def read_cached_pdf_text() -> str:
    """Load the cached PDF text if it exists, otherwise return an empty string."""
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


extract_pdf_text_tool = function_tool(extract_pdf_text)
read_cached_pdf_text_tool = function_tool(read_cached_pdf_text)
