# AI Cover Letter Generator

This project is an automated cover letter generation system powered by the Llama 3.1 (8B) model. It takes a user's resume information and a job description as input, and outputs a polished, personalized cover letter.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Prompt Templates](#prompt-templates)
6. [Deployment](#deployment)
7. [Troubleshooting](#troubleshooting)

---

## Features

* **Personalized Output**: Generates customized cover letters that highlight relevant skills and experience.


## Prerequisites

* Python 3.8 or higher
* `pip` for package management
* Hugging Face API credentials with access to the `meta-llama/Llama-3.1-8B` model (if you don't have hugging face, I have my api token in file config.json)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JiayiGao888/CoverLetterGenerator.git
   
   cd CoverLetterGenerator
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

### Streamlit Interface

Run the Streamlit app:

```bash
streamlit run app.py
```



## Prompt Templates

* **Simple Cover Letter Prompt**:

  ```text
  You are an expert in job hunting and a cover letter writer.  Be persuasive and professional. Now, generate a cover letter for a data scientist position, begin your paragraph with:I am writing to express my strong interest in the XYS company's data science position
  ```

## Model Improvement Examples

### Original Prompt Excerpt

```
I am writing to express my strong interest in the XYS company's data science position, and I am confident that I am the ideal candidate for the position. I am a skilled data scientist with experience in big data analytics and machine learning. I have a strong background in statistics and have worked on projects involving data analysis, data visualization, and data mining. I am also experienced in programming languages such as Python, R, and SQL. I have a keen eye for detail and can quickly identify patterns in large datasets. I am an excellent communicator and can easily explain complex concepts to non-technical audiences. I am confident that I can contribute to the success of your company and look forward to discussing my qualifications further. Please find attached my resume for your review. Thank you for your time and consideration. Sincerely, Your Name Your Signature Date

Cover Letter for Data Scientist
Data scientists are in high demand these days, and for good reason. They are the people who can take complex data sets and turn them into useful information. If you are looking for a job as a data scientist, you need to have a great cover letter. In this article, we will give you some tips on how to write a cover letter that will get you noticed.

The first thing you need to do is research the company you are applying to. You need to know what they do and what their goals are. This will help you tailor your cover letter to the specific needs of the company.

Once you have done your research, you need to start writing your cover letter. The first paragraph should be an introduction to who you are and why you are interested in the position. The second paragraph should be about your qualifications and how they fit the needs of the company. The third paragraph should be a summary of your experience and how it relates to the position.

Make sure to proofread your cover letter before sending it off. Typos and grammatical errors can make you look unprofessional.

If you follow these tips, you should be able to write a great cover letter that will get you noticed by the hiring manager.

Cover Letter for Data Scientist with Experience
If you are a data scientist with experience, you will want to make sure that your cover letter reflects that. Make sure to highlight your experience in your cover letter, and be sure to include any relevant skills or qualifications. Be sure to tailor your cover letter to the specific job you are applying for, and make sure to emphasize your qualifications for the position.

Cover Letter for Data Scientist with No Experience
```

### Improved Prompt Excerpt

```
I am writing to express my interest in the Tech Solutions Inc. software engineer position.

Thank you for your consideration, and I look forward to hearing from you.

I have attached my resume for your review. I can be reached at (555)-555-5555 or email at [email protected]. Thank you for your time and consideration. I look forward to hearing from you.

I am writing to express my interest in the Tech Solutions Inc. software engineer position. I am a recent graduate of the University of California, Berkeley with a degree in Computer Science. I have 3 years of experience in software development and have worked on projects involving front-end and back-end technologies. My skills include JavaScript, React, Node.js, Python, Git, Docker, and AWS. I am excited about the opportunity to join your team and contribute to your success.

My experience has given me a strong foundation in software development. I have developed and maintained web applications using React and Node.js, implemented CI/CD pipelines reducing deployment time by 40%, and collaborated with cross-functional teams to deliver features on schedule. I am confident that my skills and experience make me a strong candidate for this position.

I am eager to learn more about your company and the role you are seeking to fill. I would welcome the opportunity to discuss how my skills and experience can contribute to your success. Thank you for your time and consideration. I look forward to hearing from you.
```

## Deployment

* **Cloud Services**: Deploy the Streamlit app on ollama

## Troubleshooting

* **JSONDecodeError** -- need to fix
* **Model Loading Delays**: Consider caching the model locally or using a smaller variant for development.
* **API Rate Limits**: Monitor your Hugging Face account usage.

