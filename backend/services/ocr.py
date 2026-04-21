from PIL import Image
import pytesseract
from backend.core.config import settings
from io import BytesIO

if settings.tesseract_cmd:
    pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd

def extract_text_from_image(file_bytes: bytes) -> str:
    image = Image.open(BytesIO(file_bytes)).convert("RGB")
    return pytesseract.image_to_string(image)
