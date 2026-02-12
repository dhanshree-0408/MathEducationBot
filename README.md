# MathEducationBot
Multimodal AI Tutoring System using GPT-4, LangChain & FastAPI

# Overview

MathEducationBot is a multimodal AI-powered tutoring system designed to assist students and parents with mathematics problem-solving.
The system supports:
- Text-based queries
- Image-based queries (OCR)
- URL-based problem extraction
- Audio-based queries (Speech-to-Text)

It dynamically personalizes responses based on:
- Grade level (1–12)
- User role (Student / Parent)
- Conversational context (multi-turn memory)

# System Architecture

Flow:

User → Streamlit UI → FastAPI Backend → Query Routing Layer →
• OCR Module (Images)
• URL Parsing Module
• Speech-to-Text Module
→ LangChain + GPT-4
→ Personalized Response Generator
→ Memory Update

Key design principles:
- Modular input routing
- Separation of frontend and backend
- Context preservation using LangChain memory
- Prompt adaptation based on grade and role

<img width="324" height="255" alt="image" src="https://github.com/user-attachments/assets/c31fe9a6-0e92-4839-8517-8b724e890295" />


# Core Features
1️⃣ Multimodal Query Processing

The system detects input type and routes accordingly:
| Input Type | Processing Pipeline              |
| ---------- | -------------------------------- |
| Text       | Direct LLM processing            |
| Image      | OCR (Pytesseract) → Text → LLM   |
| URL        | HTML extraction → Cleaning → LLM |
| Audio      | SpeechRecognition → Text → LLM   |

2️⃣ Context-Aware Multi-Turn Dialogue

Implemented using:
ConversationBufferMemory (LangChain)

This allows follow-up interactions:
Example:

- User: What is derivative of x²?
- User: How does that apply to x³?

The system retains context and continues logically.

3️⃣ Grade-Level & Role Personalization

Responses adapt dynamically based on:
- Selected grade (1–12)
- User type (Student / Parent)

This influences:
- Depth of explanation
- Language complexity
- Type of examples used

4️⃣ Observability & Monitoring

Integrated with LangSmith for:
- Trace analysis
- Latency tracking
- Failure case debugging
- Response evaluation

This ensures measurable system performance rather than blind LLM usage.

# Evaluation Summary

Evaluation performed on curated real-world test queries.

Distribution:
- 40% text
- 30% image
- 15% URL
- 15% audio

Results:
| Metric                  | Score   |
| ----------------------- | ------- |
| Overall Accuracy        | 92%     |
| OCR Accuracy            | 87%     |
| F1 Score (Text Queries) | 0.89    |
| Avg Latency             | 2.4 sec |
| Interaction Score       | 93/100  |

Evaluation focuses on:
- Correctness
- Context continuity
- OCR reliability
- Latency
- Error rate

# Tech Stack

Backend:
- Python
- FastAPI
- LangChain
- OpenAI GPT-4
- Frontend:
- Streamlit

Processing:

- Pytesseract (OCR)
- SpeechRecognition (Audio)
- Requests (URL extraction)

Monitoring:

- LangSmith

# Limitations

- OCR struggles with low-quality handwriting
- Dependency on external LLM APIs
- Higher latency for image/audio queries
- No built-in feedback loop (future enhancement)

# Future Improvements

- Cloud deployment (GCP/AWS)
- Feedback scoring mechanism
- Multilingual support
- Curriculum alignment layer
- Teacher analytics dashboard
**
