"""
=========================================
Gemini Client
=========================================

Author: Soumyadip
Project: AI Health Assistant

Handles:
- Gemini API Connection
- Model Initialization
- Response Generation
- Compatibility Wrapper

=========================================
"""

import google.generativeai as genai

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


# =========================================
# CONFIGURE GEMINI
# =========================================

genai.configure(
    api_key=GEMINI_API_KEY
)


# =========================================
# LOAD MODEL
# =========================================

def get_gemini_model():
    """
    Return Gemini model instance
    """

    try:

        model = genai.GenerativeModel(
            GEMINI_MODEL
        )

        return model

    except Exception as error:

        print(
            f"Gemini Model Error: {error}"
        )

        return None


# =========================================
# GENERATE RESPONSE
# =========================================

def generate_response(prompt):
    """
    Generate AI response
    """

    try:

        model = get_gemini_model()

        if model is None:

            return (
                "❌ Unable to initialize AI model."
            )

        response = model.generate_content(
            prompt
        )

        if (
            response
            and hasattr(response, "text")
            and response.text
        ):
            return response.text

        return (
            "⚠ No response generated."
        )

    except Exception as error:

        error_text = str(error)

        if "429" in error_text:

            return (
                "⚠ Gemini API quota exceeded.\n\n"
                "Free-tier request limit reached.\n"
                "Please wait and try again later."
            )

        return (
            f"🩺 AI Error: {error_text}"
        )


# =========================================
# COMPATIBILITY WRAPPER
# =========================================

def ask_gemini(prompt):
    """
    Compatibility function
    Older modules can use:
    ask_gemini(prompt)
    """

    return generate_response(prompt)


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    question = (
        "What are common symptoms of flu?"
    )

    answer = ask_gemini(
        question
    )

    print("\nAI Response:\n")

    print(answer)