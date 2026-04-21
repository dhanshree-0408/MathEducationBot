import streamlit as st
import requests
import uuid
import os

st.set_page_config(page_title="MathEdu AI", page_icon="🧠", layout="wide")
# BACKEND_URL = st.secrets.get("BACKEND_URL", os.getenv("BACKEND_URL", "http://127.0.0.1:8000"))
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
if hasattr(st, "secrets") and "BACKEND_URL" in st.secrets:
    BACKEND_URL = st.secrets["BACKEND_URL"]

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
if "role" not in st.session_state:
    st.session_state.role = "Student"
if "grade" not in st.session_state:
    st.session_state.grade = "Grade 10"
if "source" not in st.session_state:
    st.session_state.source = "text"

st.markdown("""
<style>
.block-container {padding-top: 1.5rem;}
.hero {background: linear-gradient(135deg,#0f172a,#1d4ed8); color: white; padding: 24px; border-radius: 18px;}
.card {background: #0b1220; border: 1px solid #24324a; border-radius: 16px; padding: 16px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>MathEdu AI</h1><p>Multimodal math tutor for students and parents.</p></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.session_state.role = st.selectbox("Role", ["Student", "Parent"], index=0)
with col2:
    grades = [f"Grade {i}" for i in range(1,13)]
    st.session_state.grade = st.selectbox("Grade", grades, index=9)
with col3:
    st.session_state.source = st.selectbox("Input Type", ["text", "image", "url", "audio"], index=0)

st.markdown('<div class="card">', unsafe_allow_html=True)
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
st.markdown('</div>', unsafe_allow_html=True)

message = ""
file = None
url_text = ""
audio = None

if st.session_state.source == "text":
    message = st.chat_input("Ask a math question...")
elif st.session_state.source == "url":
    url_text = st.text_input("Paste a web URL containing the math problem")
    message = st.chat_input("Add any extra instructions...")
elif st.session_state.source == "image":
    file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg", "webp"])
    message = st.chat_input("Add context for the uploaded image...")
elif st.session_state.source == "audio":
    audio = st.audio_input("Record your question")
    message = st.chat_input("Add context after recording...")

submit = st.button("Generate Answer", use_container_width=True)

if submit:
    payload = {"session_id": st.session_state.session_id, "message": message or "", "role": st.session_state.role, "grade": st.session_state.grade, "source": st.session_state.source, "url": url_text}
    files = {}
    if file is not None:
        files["image"] = (file.name, file.getvalue(), file.type)
    if st.session_state.source == "audio" and audio is not None:
        files["audio"] = ("audio.wav", audio.getvalue(), "audio/wav")
    # r = requests.post(f"{BACKEND_URL}/api/chat", data=payload, files=files, timeout=120)
    # data = r.json()

    r = requests.post(f"{BACKEND_URL}/api/chat", data=payload, files=files, timeout=120)

    if r.status_code != 200:
        st.error(f"Backend error {r.status_code}")
        st.code(r.text)
    else:
        try:
            data = r.json()
            st.session_state.messages.append({"role": "user", "content": message or url_text or st.session_state.source})
            st.session_state.messages.append({"role": "assistant", "content": data.get("answer", "No answer")})
            st.rerun()
        except ValueError:
            st.error("Backend did not return valid JSON.")
            st.code(r.text)

    st.session_state.messages.append({"role": "user", "content": message or url_text or st.session_state.source})
    st.session_state.messages.append({"role": "assistant", "content": data.get("answer", "No answer")})
    st.rerun()

st.sidebar.title("Session")
st.sidebar.write("Session ID:", st.session_state.session_id)
st.sidebar.write("Backend:", BACKEND_URL)
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
