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

/* Fix chat message text color */
[data-testid="stChatMessage"] {
    color: #1f2933 !important;
}

/* Fix assistant message specifically */
[data-testid="stChatMessage"] p {
    color: #1f2933 !important;
}

/* Fix markdown text inside chat */
[data-testid="stMarkdownContainer"] {
    color: #1f2933 !important;
}

/* User message bubble */
[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
    color: #1f2933 !important;
}

/* Assistant message bubble */
[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
    color: #1f2933 !important;
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