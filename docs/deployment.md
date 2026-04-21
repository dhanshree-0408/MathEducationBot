## Deployment Guide

### Backend
uvicorn backend.main:app --host 0.0.0.0 --port $PORT

### Frontend
streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0

### Environment Variables
- OPENAI_API_KEY
- OPENAI_MODEL
- DATABASE_URL
- BACKEND_URL
- TESSERACT_CMD
