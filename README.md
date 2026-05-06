# MathEducationBot

MathEducationBot is an AI-powered math tutoring project built with FastAPI, Streamlit, and OpenAI. It helps users solve math questions in a simple, interactive way and supports multiple input styles such as text, image, URL, and audio.

## Project Overview

This project was built as part of my M.Tech thesis work. The main idea was to create a helpful math assistant that can guide students and parents through math problems instead of just giving direct answers.

The system is designed to make math learning more accessible, interactive, and personalized. It can adjust responses based on the user’s role and grade level, and it also keeps chat history for better context in follow-up questions.

## Features

- Text-based math question support
- Image-based question input using OCR
- URL-based question extraction
- Audio-based question input
- Role-based responses for student and parent
- Grade-level aware answers
- Chat history saving
- FastAPI backend
- Streamlit frontend
- OpenAI API integration

## Tech Stack

- Python
- FastAPI
- Streamlit
- OpenAI API
- LangChain
- Pytesseract
- SpeechRecognition
- SQLite
- Requests
- BeautifulSoup

## How It Works

1. User enters a math question using text, image, URL, or audio.
2. The backend identifies the input type and processes it.
3. OCR is used for image-based inputs.
4. Web content is extracted for URL-based inputs.
5. Audio is converted to text.
6. The processed question is sent to OpenAI for a helpful response.
7. The answer is shown in the Streamlit UI and saved in chat history.

## Why I Built This

I built this project to explore how AI can support learning in a more practical and user-friendly way. Instead of just giving final answers, the goal was to provide guided help that supports understanding and learning.

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/dhanshree-0408/MathEducationBot.git
cd MathEducationBot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:
```bash
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add environment variables
Create a `.env` file and add:
```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
DATABASE_URL=sqlite:///./mathedu_ai.db
BACKEND_URL=http://127.0.0.1:8000
```

### 5. Run the backend
```bash
uvicorn backend.main:app --reload --port 8000
```

### 6. Run the frontend
```bash
streamlit run frontend/app.py
```

## Future Improvements

- Login and authentication
- Export chat history
- Better math formatting
- Streaming responses
- More advanced answer explanation flow

## Note

This is a thesis-based project and is still open for improvement. I will continue enhancing it with more practical features and a better user experience.
