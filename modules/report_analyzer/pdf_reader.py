import streamlit as st
import PyPDF2
import os


# ==========================================
# PDF TEXT EXTRACTION FUNCTION
# ==========================================
def extract_text_from_pdf(file):

    try:
        pdf_reader = PyPDF2.PdfReader(file)

        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


# ==========================================
# STREAMLIT UI
# ==========================================
def show_pdf_reader_page():

    st.title("📄 Medical PDF Reader")
    st.caption("Upload medical reports or documents to extract text")

    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("File uploaded successfully ✔")

        # Show file details
        st.write("📁 File Name:", uploaded_file.name)
        st.write("📦 File Size:", uploaded_file.size, "bytes")

        # Extract text
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)

        st.markdown("---")

        st.subheader("📜 Extracted Text")

        if text:
            st.text_area("PDF Content", text, height=400)
        else:
            st.warning("No text found in PDF")

        # Optional download extracted text
        st.download_button(
            label="⬇ Download Extracted Text",
            data=text,
            file_name="extracted_report.txt",
            mime="text/plain"
        )