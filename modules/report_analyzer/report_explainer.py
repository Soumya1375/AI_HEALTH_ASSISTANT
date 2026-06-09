import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ==========================================
# LOAD GEMINI API
# ==========================================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================
# AI REPORT EXPLAINER FUNCTION
# ==========================================
def explain_report(text):

    prompt = f"""
    You are a professional medical AI assistant.

    Your task:
    - Explain the medical report in simple language
    - Highlight important health issues if any
    - Summarize key findings
    - Suggest basic lifestyle advice (not diagnosis)

    Medical Report:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


# ==========================================
# STREAMLIT UI
# ==========================================
def show_report_explainer_page():

    st.title("🧠 AI Report Explainer")
    st.caption("Understand your medical reports in simple language")

    # INPUT OPTION 1: TEXT PASTE
    report_text = st.text_area("Paste Medical Report Text Here", height=250)

    # INPUT OPTION 2: FILE UPLOAD (OPTIONAL)
    uploaded_file = st.file_uploader("Or Upload Text File", type=["txt"])

    final_text = ""

    if uploaded_file is not None:
        final_text = str(uploaded_file.read(), "utf-8")
    elif report_text:
        final_text = report_text

    st.markdown("---")

    if st.button("Explain Report"):

        if final_text:

            with st.spinner("AI is analyzing your report..."):

                try:
                    explanation = explain_report(final_text)

                    st.success("Analysis Completed ✔")

                    st.subheader("📊 AI Explanation")
                    st.write(explanation)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.warning("Please provide report text or upload a file")