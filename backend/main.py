from fastapi import FastAPI
from backend.core.config import settings
from backend.storage.db import init_db
from backend.routers import health, chat, history

app = FastAPI(title=settings.app_name, version="1.0.0")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(health.router)
app.include_router(chat.router, prefix="/api")
app.include_router(history.router, prefix="/api")
