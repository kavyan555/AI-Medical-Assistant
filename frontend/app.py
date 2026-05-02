import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Medical Assistant", layout="wide")

st.title("🩺 AI Medical Assistant (Llama 3)")

# Upload section
with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose file", type=["pdf"])

    if uploaded_file and st.button("Upload"):
        files = {"file": uploaded_file.getvalue()}
        requests.post(f"{API_URL}/upload", files=files)
        st.success("Indexed successfully!")

# Chat
st.subheader("Ask Questions")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Enter your question")

if st.button("Ask") and query:
    res = requests.post(f"{API_URL}/ask", params={"query": query})
    answer = res.json()["answer"]
    st.session_state.chat.append((query, answer))

for q, a in st.session_state.chat:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 AI:** {a}")