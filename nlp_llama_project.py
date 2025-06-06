# -*- coding: utf-8 -*-
"""nlp_llama_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ifumFDU3GelK71vLo0ivfGLqNzZhcOhA
"""

!pip install -r requirements.txt

pip install hf_xet

import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig,pipeline

#building llama model, I got the token by requesting it from hugging face llama community

config_data = json.load(open("config.json"))
HF_TOKEN = config_data["HF_TOKEN"]
model_name="meta-llama/Llama-3.1-8B"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, #more efficient compared with 8 bits
    bnb_4bit_use_double_quant=True, #doesn't make the model loose too much information / performance score
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_name,
                                          token=HF_TOKEN)

tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config,
    token=HF_TOKEN
)

text_generator = pipeline(
    "text-generation", #different piplines, google and search transformers piplines
    model=model,
    tokenizer=tokenizer,
    min_new_tokens=300
)

text_generator = pipeline(
    "text-generation", #different piplines, google and search transformers piplines
    model=model,
    tokenizer=tokenizer,
    min_new_tokens=300
)

prompt = "You are an expert in job hunting and a cover letter writer.  Be persuasive and professional. Now, generate a cover letter for a data scientist position, begin your paragraph with:I am writing to express my strong interest in the XYS company's data science position"

output = text_generator(
    prompt,
    max_new_tokens=500,
    min_new_tokens=260,
    pad_token_id=tokenizer.eos_token_id
)

output

"""we see the first one didn't have enough information to generate a full cover letter**Now try it with a better written Prompt with more information given**"""

prompt = '''You are a professional cover letter writing assistant. Using information provided below and the job description, create a personalized cover letter. Do not repeat yourself

name of the applicant: Jiayi Gao
experience: title: Software Engineer,
        "responsibilities":
            "Developed and maintained web applications using React and Node.js",
            "Implemented CI/CD pipelines reducing deployment time by 40%",
            "Collaborated with cross-functional teams to deliver features on schedule"

"education": degree": "Bachelor of Science in Computer Science",

"skills":JavaScript", "React", "Node.js", "Python", "Git", "Docker", "AWS"

job Description:Software Engineer - Full Stack\nWe are seeking a talented software engineer to join our team. The ideal Requirements:\n- 3+ years of experience in software development\n- Strong knowledge of JavaScript and frameworks like React\n- Experience with back-end technologies (Node.js preferred)
start the cover letter as: I am writing to express my interest in the Tech Solutions Inc. software engineer position.

'''

output = text_generator(
    prompt,
    max_new_tokens=500,
    min_new_tokens=260,
    pad_token_id=tokenizer.eos_token_id
)
output

"""## **This simple model does generate a okay cover letter, but I want to generate a more complexed model with the same llama model**

"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile file_loader.py
# 
# # to convert cover letter from pdf/doc to plain text
# import os
# from docx import Document
# import PyPDF2
# 
# def read_docx(file_path):
#     """Reads a .docx file and returns the text content."""
#     try:
#         doc = Document(file_path)
#         text = []
#         for paragraph in doc.paragraphs:
#             text.append(paragraph.text)
#         return '\n'.join(text)
#     except Exception as e:
#         return f"Error reading .docx file: {e}"
# 
# def read_pdf(file_path):
#     """Reads a .pdf file and returns the text content."""
#     try:
#         with open(file_path, 'rb') as pdf_file:
#             reader = PyPDF2.PdfReader(pdf_file)
#             text = []
#             for page in reader.pages:
#                 text.append(page.extract_text())
#             return '\n'.join(text)
#     except Exception as e:
#         return f"Error reading .pdf file: {e}"
# 
# def read_document(file_path):
#     """Determines the file type and reads the document accordingly."""
#     if not os.path.exists(file_path):
#         return "File not found. Please check the file path."
# 
#     _, file_extension = os.path.splitext(file_path)
# 
#     if file_extension.lower() == '.docx':
#         return read_docx(file_path)
#     elif file_extension.lower() == '.pdf':
#         return read_pdf(file_path)
#     else:
#         return "Unsupported file format. Please use .docx or .pdf."

# Commented out IPython magic to ensure Python compatibility.
# %%writefile cover_letter.py
# 
# import json
# import ast
# import torch
# from transformers import (
#     AutoTokenizer,
#     AutoModelForCausalLM,
#     BitsAndBytesConfig,
#     pipeline
# )
# from datetime import datetime
# from file_loader import read_document
# 
# # Load prompt templates once at module import
# with open("resume_parser_api.json") as f:
#     _resume_api = json.load(f)
# RESUME_TEMPLATE = _resume_api["messages"][0]["content"]
# 
# with open("cover_letter_api.json") as f:
#     _cover_api = json.load(f)
# COVER_TEMPLATE = _cover_api["messages"][0]["content"]
# 
# 
# _config = json.load(open("config.json"))
# HF_TOKEN   = _config["HF_TOKEN"]
# MODEL_NAME = "meta-llama/Llama-3.1-8B"
# 
# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.float16
# )
# 
# class CoverLetterAI:
#     def __init__(self):
#         self.model = AutoModelForCausalLM.from_pretrained(
#             MODEL_NAME,
#             device_map="auto",
#             quantization_config=bnb_config,
#             use_auth_token=HF_TOKEN
#         )
# 
#         self.tokenizer = AutoTokenizer.from_pretrained(
#             MODEL_NAME,
#             use_auth_token=HF_TOKEN
#         )
#         self.tokenizer.pad_token = self.tokenizer.eos_token
#         #create generation pipeline
#         self.generator = pipeline(
#             "text-generation",
#             model=self.model,
#             tokenizer=self.tokenizer,
#             device_map="auto"
#         )
# 
#         self.date_today = datetime.today().strftime("%d - %b - %Y")
# 
#     def read_candidate_data(self, resume_file_path: str):
#         """
#         Read the user's resume (PDF or DOCX) into memory.
#         """
#         self.resume = read_document(resume_file_path)
# 
# # this function still fails when passing correctly formatted JSON to the Transformer text-generation pipeline
#     def profile_candidate(self) -> str:
#         """
#         Extract structured profile information from the resume.
#         Returns a pretty-printed JSON string.
#         """
#         prompt = (
#             RESUME_TEMPLATE
#             + "\n\nResume:\n"
#             + self.resume
#             + "\n\nReturn *only* the JSON object."
#         )
#         response = self.generator(
#             prompt,
#             max_new_tokens=512,
#             pad_token_id=self.tokenizer.eos_token_id,
#             temperature=0.0,
#             do_sample=False
#         )
#         output = response[0]["generated_text"]
# 
#         # find the first {…} block
#         start = output.find("{")
#         end   = output.rfind("}") + 1
#         raw_json = output[start:end] if start>=0 and end>0 else ""
# 
#         try:
#             profile_data = json.loads(raw_json)
#             self.profile_dict = profile_data
#             self.profile_str  = json.dumps(profile_data, indent=2)
#             return self.profile_str
#         except json.JSONDecodeError:
#             return output
# 
# 
#     def add_job_description(self, job_description: str):
#         """
#         Store the user's target job description for the cover letter.
#         """
#         self.job_description = job_description
# 
#     def write_cover_letter(self) -> str:
#         """
#         Generate a cover letter using the parsed profile, job description,
#         and today's date.
#         """
#         prompt = COVER_TEMPLATE.format(
#             resume_json=self.profile_str,
#             job_description=self.job_description,
#             date=self.date_today
#         )
#         response = self.generator(
#             prompt,
#             max_new_tokens=512,
#             pad_token_id=self.tokenizer.eos_token_id,
#             temperature=0.0,
#             do_sample=False
#         )
#         cover = response[0]["generated_text"].strip()
#         return cover
#

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# import os
# from cover_letter import CoverLetterAI
# 
# # App Styling & Config
# st.set_page_config(page_title="AI Cover Letter Generator", page_icon="🦾", layout="centered")
# 
# # Custom CSS for UI Styling
# st.markdown(
#     """
#     <style>
#         .main { background-color: #f9f9f9; }
#         .stTextArea textarea { font-size: 14px; }
#         .stButton button { font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; border-radius: 8px; }
#         .stButton button:hover { background-color: #45a049; }
#         .stTextInput input { font-size: 14px; }
#         .footer { font-size: 14px; text-align: center; padding-top: 20px; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# 
# # Title and Description
# st.markdown("<h1 style='text-align: center;'>📄 AI Cover Letter Generator</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size: 18px;'>Upload your resume and job description, and let AI craft a professional cover letter.</p>", unsafe_allow_html=True)
# 
# # File Upload
# st.subheader("📂 Upload Your Resume")
# uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])
# 
# if uploaded_file is not None:
#     # Save uploaded file temporarily
#     temp_file_path = f"temp_{uploaded_file.name}"
#     with open(temp_file_path, "wb") as temp_file:
#         temp_file.write(uploaded_file.read())
# 
#     # Process file with CoverLetterAI
#     cover_letter_ai = CoverLetterAI()
#     cover_letter_ai.read_candidate_data(temp_file_path)
# 
#     # Remove temp file after processing
#     os.remove(temp_file_path)
# 
#     # Display Extracted Resume Information
#     st.subheader("🔍 Extracted Resume Information")
#     with st.spinner("Analyzing your resume..."):
#         profile = cover_letter_ai.profile_candidate()
#     st.text_area("Your Profile", profile, height=300)
# 
#     # Job Description Input
#     st.subheader("📌 Job Description")
#     job_description = st.text_area(
#         "Paste the job description here", "", height=200
#     )
# 
#     # Generate Cover Letter
#     if st.button("✍️ Generate Cover Letter") and job_description:
#         cover_letter_ai.add_job_description(job_description)
#         with st.spinner("Generating your cover letter..."):
#             cover_letter = cover_letter_ai.write_cover_letter()
#         st.subheader("✨ Your Custom Cover Letter")
#         st.text_area("Cover Letter", cover_letter, height=300)
# 
# # Footer
# st.markdown(
#     """
#     <div class="footer">
#         <p>For NLP Class Project</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

!wget -q -O - ipv4.icanhazip.com

"""copy the output from cell 24 to the website to streamlit, for this model, I unfortunately failed to match the JSON file to transformer pipeline"""

!streamlit run app.py & npx localtunnel --port 8501