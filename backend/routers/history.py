from fastapi import APIRouter
from backend.storage.repository import get_history

router = APIRouter()

@router.get("/history/{session_id}")
def history(session_id: str):
    rows = get_history(session_id, limit=50)
    return {
        "session_id": session_id,
        "items": [
            {"user_message": r.user_message, "assistant_message": r.assistant_message, "source": r.source, "role": r.role, "grade": r.grade} for r in rows
        ]
    }
