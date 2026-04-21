from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_name: str = "MathEdu AI"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./mathedu_ai.db")
    backend_url: str = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    tesseract_cmd: str = os.getenv("TESSERACT_CMD", "")

settings = Settings()
