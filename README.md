# MathEdu AI

A recruiter-friendly multimodal math tutor built with FastAPI, Streamlit, OpenAI, OCR, URL extraction, audio transcription, and persistent history.

## Features
- Text, image, URL, and audio query support
- Student/parent role personalization
- Grade-aware responses
- Persistent chat history with SQLite
- FastAPI backend + Streamlit frontend
- Clean deployable repo structure

## Local setup
1. Create a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI key.
4. Start backend: `uvicorn backend.main:app --reload --port 8000`
5. Start frontend: `streamlit run frontend/app.py`

## macOS notes
- Install Tesseract: `brew install tesseract`
- If needed, set `TESSERACT_CMD` in `.env` to the installed binary path.

## Windows notes
- Install Tesseract from the official installer.
- Add Tesseract to PATH or set `TESSERACT_CMD` in `.env`.

## Deployment
- Backend: Render, Railway, Fly.io
- Frontend: Streamlit Community Cloud or Render
- Set `BACKEND_URL` to your backend URL
