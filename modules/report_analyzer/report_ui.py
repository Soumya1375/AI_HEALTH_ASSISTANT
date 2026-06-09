import streamlit as st
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv
import os
from io import BytesIO

from modules.report_analyzer.pdf_reader import extract_text_from_pdf
from modules.report_analyzer.report_explainer import explain_report


# ==========================================
# LOAD GEMINI
# ==========================================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================
# GEMINI REPORT GENERATOR
# ==========================================
def generate_ai_report(text, name, age):

    prompt = f"""
    You are a professional medical AI report generator.

    Create a structured health report with:

    1. Patient Summary
    2. Key Findings
    3. Risk Level (Low / Medium / High)
    4. Health Recommendations
    5. Simple explanation

    Patient Name: {name}
    Age: {age}

    Medical Data:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


# ==========================================
# STREAMLIT UI
# ==========================================
def show_report_analyzer_page():

    st.title("📄 AI Health Report Analyzer")
    st.caption("Upload or paste medical data for AI-powered health report")

    # ==========================================
    # USER INPUT
    # ==========================================
    name = st.text_input("👤 Patient Name")
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=18)

    st.markdown("---")

    # INPUT OPTIONS
    uploaded_pdf = st.file_uploader("📂 Upload Medical PDF", type=["pdf"])
    pasted_text = st.text_area("✍ Or Paste Medical Report Text", height=200)

    final_text = ""

    if uploaded_pdf:
        final_text = extract_text_from_pdf(uploaded_pdf)

    elif pasted_text:
        final_text = pasted_text

    st.markdown("---")

    # ==========================================
    # GENERATE REPORT
    # ==========================================
    if st.button("🚀 Generate AI Health Report"):

        if not name:
            st.warning("Please enter patient name")
            st.stop()

        if not final_text:
            st.warning("Please provide medical data (PDF or text)")
            st.stop()

        with st.spinner("🧠 AI is analyzing medical data..."):

            try:
                ai_report = generate_ai_report(final_text, name, age)

                st.success("Report Generated Successfully ✔")

                # ==========================================
                # SHOW REPORT
                # ==========================================
                st.subheader("📊 AI Generated Health Report")
                st.write(ai_report)

                # ==========================================
                # AI EXPLANATION (SECOND LAYER)
                # ==========================================
                st.subheader("🧠 Simplified Explanation")

                explanation = explain_report(final_text)
                st.info(explanation)

                # ==========================================
                # TIMESTAMP
                # ==========================================
                st.caption(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                # ==========================================
                # DOWNLOAD TXT
                # ==========================================
                st.download_button(
                    label="⬇ Download Report (TXT)",
                    data=ai_report,
                    file_name=f"{name}_health_report.txt",
                    mime="text/plain"
                )

                # ==========================================
                # DOWNLOAD PDF (SIMPLE VERSION)
                # ==========================================
                def create_pdf(text):
                    from reportlab.lib.pagesizes import letter
                    from reportlab.pdfgen import canvas

                    buffer = BytesIO()
                    c = canvas.Canvas(buffer, pagesize=letter)
                    width, height = letter

                    y = height - 40

                    for line in text.split("\n"):
                        c.drawString(40, y, line[:100])
                        y -= 15
                        if y < 40:
                            c.showPage()
                            y = height - 40

                    c.save()
                    buffer.seek(0)
                    return buffer

                pdf_file = create_pdf(ai_report)

                st.download_button(
                    label="⬇ Download Report (PDF)",
                    data=pdf_file,
                    file_name=f"{name}_health_report.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")