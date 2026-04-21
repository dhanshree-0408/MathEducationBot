import speech_recognition as sr
from tempfile import NamedTemporaryFile

def transcribe_audio_bytes(audio_bytes: bytes) -> str:
    recognizer = sr.Recognizer()
    with NamedTemporaryFile(delete=True, suffix=".wav") as f:
        f.write(audio_bytes)
        f.flush()
        with sr.AudioFile(f.name) as source:
            audio = recognizer.record(source)
    return recognizer.recognize_google(audio)
