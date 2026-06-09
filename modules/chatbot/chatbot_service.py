"""
=========================================
Health Chatbot Service (PRO VERSION)
=========================================
"""

from modules.chatbot.gemini_client import generate_response
from database.db import execute_query


# =========================================
# SYSTEM PROMPT (PRO DOCTOR MODE)
# =========================================

SYSTEM_PROMPT = """
You are a Professional AI Health Assistant (Doctor-like advisor, NOT a real doctor).

Rules:
1. Do NOT claim to be a real doctor
2. Do NOT diagnose diseases
3. Do NOT prescribe medications
4. Provide only educational guidance
5. Always suggest consulting a healthcare professional for serious issues
6. Be calm, structured, and easy to understand
7. Prioritize user safety at all times

Response Format:
1. 🧾 Summary
2. 🔍 Possible Causes
3. 🏡 Home Care Suggestions
4. ⚠️ Warning Signs
5. 🏥 Final Advice
"""


# =========================================
# EMERGENCY KEYWORDS
# =========================================

EMERGENCY_KEYWORDS = [
    "chest pain",
    "heart attack",
    "stroke",
    "difficulty breathing",
    "shortness of breath",
    "unconscious",
    "seizure",
    "severe bleeding",
    "suicidal",
    "emergency",
    "can't breathe",
    "fainting"
]


# =========================================
# EMERGENCY CHECK
# =========================================

def is_emergency(user_message: str) -> bool:
    message = user_message.lower()
    return any(keyword in message for keyword in EMERGENCY_KEYWORDS)


# =========================================
# EMERGENCY RESPONSE
# =========================================

def get_emergency_response():
    return """
🚨 EMERGENCY ALERT 🚨

Your symptoms may indicate a serious medical condition.

👉 Please seek immediate medical attention
👉 Visit nearest hospital or call emergency services

⚠ This AI cannot handle emergency situations.
"""


# =========================================
# CHAT SAVE (optional logging)
# =========================================

def save_chat(question, answer, user_id=None):

    try:
        query = """
        INSERT INTO chat_history
        (user_id, question, answer)
        VALUES (?, ?, ?)
        """

        execute_query(query, (user_id, question, answer))

    except Exception as e:
        print("Chat save error:", e)


# =========================================
# MAIN AI FUNCTION (PRO LOGIC)
# =========================================

def ask_health_assistant(user_message, user_id=None):

    # Step 1: Emergency check
    if is_emergency(user_message):
        response = get_emergency_response()

        save_chat(user_message, response, user_id)
        return response

    # Step 2: Build final prompt
    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{user_message}

Provide structured medical guidance.
"""

    # Step 3: AI response
    response = generate_response(prompt)

    # Step 4: Safe disclaimer
    response += """

------------------------------------------------
⚠ Disclaimer:
This is for educational purposes only.
Not a substitute for professional medical advice.
"""

    # Step 5: Save chat
    save_chat(user_message, response, user_id)

    return response


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    question = "I have fever and headache"

    answer = ask_health_assistant(question)

    print("\nAI RESPONSE:\n")
    print(answer)