from openai import OpenAI
from backend.core.config import settings
from backend.core.prompts import SYSTEM_PROMPT, build_user_prompt

client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

def generate_answer(question: str, role: str, grade: str, source: str, context: str = "") -> str:
    if not client:
        return "OpenAI API key is not configured. Add OPENAI_API_KEY to your .env file."
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_user_prompt(question, role, grade, source, context)},
    ]
    response = client.chat.completions.create(model=settings.openai_model, messages=messages, temperature=0.2)
    return response.choices[0].message.content or "No response returned."
