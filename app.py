
import streamlit as st
import os
from cover_letter import CoverLetterAI

# App Styling & Config
st.set_page_config(page_title="AI Cover Letter Generator", page_icon="🦾", layout="centered")

# Custom CSS for UI Styling
st.markdown(
    """
    <style>
        .main { background-color: #f9f9f9; }
        .stTextArea textarea { font-size: 14px; }
        .stButton button { font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; border-radius: 8px; }
        .stButton button:hover { background-color: #45a049; }
        .stTextInput input { font-size: 14px; }
        .footer { font-size: 14px; text-align: center; padding-top: 20px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1 style='text-align: center;'>📄 AI Cover Letter Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Upload your resume and job description, and let AI craft a professional cover letter.</p>", unsafe_allow_html=True)

# File Upload
st.subheader("📂 Upload Your Resume")
uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())

    # Process file with CoverLetterAI
    cover_letter_ai = CoverLetterAI()
    cover_letter_ai.read_candidate_data(temp_file_path)

    # Remove temp file after processing
    os.remove(temp_file_path)

    # Display Extracted Resume Information
    st.subheader("🔍 Extracted Resume Information")
    with st.spinner("Analyzing your resume..."):
        profile = cover_letter_ai.profile_candidate()
    st.text_area("Your Profile", profile, height=300)

    # Job Description Input
    st.subheader("📌 Job Description")
    job_description = st.text_area(
        "Paste the job description here", "", height=200
    )

    # Generate Cover Letter
    if st.button("✍️ Generate Cover Letter") and job_description:
        cover_letter_ai.add_job_description(job_description)
        with st.spinner("Generating your cover letter..."):
            cover_letter = cover_letter_ai.write_cover_letter()
        st.subheader("✨ Your Custom Cover Letter")
        st.text_area("Cover Letter", cover_letter, height=300)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>For NLP Class Project</p>
    </div>
    """,
    unsafe_allow_html=True
)
