from fastapi import APIRouter, UploadFile, File, Form
from backend.schemas.chat import ChatResponse
from backend.storage.repository import save_chat, get_history
from backend.services.router import resolve_source
from backend.services.llm import generate_answer

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(session_id: str = Form(...), message: str = Form(""), role: str = Form("Student"), grade: str = Form("Grade 10"), source: str = Form("text"), url: str = Form(""), image: UploadFile | None = File(None), audio: UploadFile | None = File(None)):
    image_bytes = await image.read() if image else None
    audio_bytes = await audio.read() if audio else None
    resolved = resolve_source(message, source, image_bytes=image_bytes, url=url, audio_bytes=audio_bytes)
    history = get_history(session_id, limit=8)
    context = "\n".join([f"User: {h.user_message}\nAssistant: {h.assistant_message}" for h in history])
    answer = generate_answer(resolved, role, grade, source, context)
    save_chat(session_id, role, grade, source, resolved, answer)
    return ChatResponse(session_id=session_id, answer=answer, source=source, role=role, grade=grade)
