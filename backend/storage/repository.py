from backend.storage.db import SessionLocal
from backend.models.history import ChatEntry

def save_chat(session_id, role, grade, source, user_message, assistant_message):
    db = SessionLocal()
    item = ChatEntry(session_id=session_id, role=role, grade=grade, source=source, user_message=user_message, assistant_message=assistant_message)
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return item

def get_history(session_id, limit=12):
    db = SessionLocal()
    rows = db.query(ChatEntry).filter(ChatEntry.session_id == session_id).order_by(ChatEntry.id.desc()).limit(limit).all()
    db.close()
    return list(reversed(rows))
