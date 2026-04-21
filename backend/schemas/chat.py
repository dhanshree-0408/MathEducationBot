from pydantic import BaseModel

class ChatResponse(BaseModel):
    session_id: str
    answer: str
    source: str
    role: str
    grade: str
