from backend.services.ocr import extract_text_from_image
from backend.services.url_fetcher import extract_text_from_url
from backend.services.audio import transcribe_audio_bytes

def resolve_source(message: str, source: str, image_bytes=None, url: str = "", audio_bytes=None):
    if source == "image" and image_bytes:
        return extract_text_from_image(image_bytes)
    if source == "url" and url:
        return extract_text_from_url(url)
    if source == "audio" and audio_bytes:
        return transcribe_audio_bytes(audio_bytes)
    return message
