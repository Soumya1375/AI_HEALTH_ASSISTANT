import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ✅ USE YOUR SERVICE LAYER (IMPORTANT)
from modules.chatbot.chatbot_service import ask_health_assistant


# =====================================
# LOAD ENV
# =====================================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


# =====================================
# CHAT UI
# =====================================
def show_chatbot_page():

    # =========================
    # CSS STYLING (PRO UI)
    # =========================
    st.markdown("""
    <style>

    .chat-title {
        font-size: 34px;
        font-weight: 800;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 5px;
    }

    .chat-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 25px;
    }

    .user-msg {
        background: linear-gradient(135deg, #d4fc79, #96e6a1);
        padding: 12px;
        border-radius: 12px;
        margin: 6px 0;
        font-size: 15px;
    }

    .bot-msg {
        background: linear-gradient(135deg, #f1f0f0, #e0e0e0);
        padding: 12px;
        border-radius: 12px;
        margin: 6px 0;
        font-size: 15px;
    }

    .chat-container {
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HEADER
    # =========================
    st.markdown('<div class="chat-title">🩺 AI Doctor Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-subtitle">Smart Health AI with Emergency Detection</div>', unsafe_allow_html=True)

    # =========================
    # SESSION MEMORY
    # =========================
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # =========================
    # INPUT
    # =========================
    user_input = st.chat_input("Ask your health question...")

    # =========================
    # PROCESS INPUT (SMART MODE)
    # =========================
    if user_input:

        # Save user msg
        st.session_state.chat_history.append(("user", user_input))

        # 🔥 CALL SERVICE LAYER (PRO LOGIC)
        bot_reply = ask_health_assistant(
            user_input,
            user_id=st.session_state.get("user", None)
        )

        # Save bot msg
        st.session_state.chat_history.append(("bot", bot_reply))

    # =========================
    # DISPLAY CHAT HISTORY
    # =========================
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for role, msg in st.session_state.chat_history:

        if role == "user":
            st.markdown(f'<div class="user-msg">🧑 {msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">🩺 {msg}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)