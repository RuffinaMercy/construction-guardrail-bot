import streamlit as st
from dotenv import load_dotenv
from src_2.chatbot import Chatbot

load_dotenv()

st.set_page_config(
    page_title="Construction Assistant",
    page_icon="🏗️",
    layout="wide"
)

# UI Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Manrope', sans-serif;
    }

    .main {
        background: radial-gradient(circle at 20% 10%, #dff5e3 0%, #f7fbf8 50%, #eef3ef 100%);
    }

    .hero {
        border: 1px solid #c6d8cb;
        background: linear-gradient(120deg, #eef8f0, #f8faf7);
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-bottom: 1rem;
    }

    .note {
        border-left: 4px solid #2f7a58;
        padding: 0.6rem 0.8rem;
        background: #f0faf4;
        border-radius: 6px;
        color: #1d3328;
        margin-top: 0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state
if "bot" not in st.session_state:
    st.session_state.bot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown("""
<div class="hero">
  <h2 style="margin:0; color:#143225;">🏗️ Construction Assistant</h2>
  <p style="margin:6px 0 0 0; color:#254536;">
    Ask anything about construction, materials, cost, design, foundation, or safety.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='note'><b>Scope:</b> Only construction-related queries are supported.</div>",
    unsafe_allow_html=True,
)

# Chat history
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# Input
prompt = st.chat_input("Ask your construction question...")

if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.bot.ask(prompt)

    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)