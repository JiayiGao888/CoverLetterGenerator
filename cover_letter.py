
import json
import ast
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    pipeline
)
from datetime import datetime
from file_loader import read_document

# Load prompt templates once at module import
with open("resume_parser_api.json") as f:
    _resume_api = json.load(f)
RESUME_TEMPLATE = _resume_api["messages"][0]["content"]

with open("cover_letter_api.json") as f:
    _cover_api = json.load(f)
COVER_TEMPLATE = _cover_api["messages"][0]["content"]


_config = json.load(open("config.json"))
HF_TOKEN   = _config["HF_TOKEN"]
MODEL_NAME = "meta-llama/Llama-3.1-8B"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)

class CoverLetterAI:
    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="auto",
            quantization_config=bnb_config,
            use_auth_token=HF_TOKEN
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            use_auth_token=HF_TOKEN
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        #create generation pipeline
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device_map="auto"
        )

        self.date_today = datetime.today().strftime("%d - %b - %Y")

    def read_candidate_data(self, resume_file_path: str):
        """
        Read the user's resume (PDF or DOCX) into memory.
        """
        self.resume = read_document(resume_file_path)

# this function still fails when passing correctly formatted JSON to the Transformer text-generation pipeline
    def profile_candidate(self) -> str:
        """
        Extract structured profile information from the resume.
        Returns a pretty-printed JSON string.
        """
        prompt = (
            RESUME_TEMPLATE
            + "\n\nResume:\n"
            + self.resume
            + "\n\nReturn *only* the JSON object."
        )
        response = self.generator(
            prompt,
            max_new_tokens=512,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.0,
            do_sample=False
        )
        output = response[0]["generated_text"]

        # find the first {…} block
        start = output.find("{")
        end   = output.rfind("}") + 1
        raw_json = output[start:end] if start>=0 and end>0 else ""

        try:
            profile_data = json.loads(raw_json)
            self.profile_dict = profile_data
            self.profile_str  = json.dumps(profile_data, indent=2)
            return self.profile_str
        except json.JSONDecodeError:
            return output


    def add_job_description(self, job_description: str):
        """
        Store the user's target job description for the cover letter.
        """
        self.job_description = job_description

    def write_cover_letter(self) -> str:
        """
        Generate a cover letter using the parsed profile, job description,
        and today's date.
        """
        prompt = COVER_TEMPLATE.format(
            resume_json=self.profile_str,
            job_description=self.job_description,
            date=self.date_today
        )
        response = self.generator(
            prompt,
            max_new_tokens=512,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.0,
            do_sample=False
        )
        cover = response[0]["generated_text"].strip()
        return cover
