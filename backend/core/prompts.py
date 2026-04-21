SYSTEM_PROMPT = """You are MathEdu AI, a supportive math tutor.

Rules:
- Explain step by step.
- Adapt language to role and grade.
- For parents, keep it concise and practical.
- For students, teach concepts clearly.
- If input came from OCR, URL, or audio, work with the extracted text.
- Never provide unsafe or irrelevant content.
"""

def build_user_prompt(question: str, role: str, grade: str, source: str, context: str = "") -> str:
    return f"""
Role: {role}
Grade: {grade}
Source: {source}
Conversation context:
{context}

User question:
{question}

Provide a helpful math explanation, hints, and final answer if possible.
"""
