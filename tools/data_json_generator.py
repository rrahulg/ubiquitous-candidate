import os
import re
import sys

import fitz
import google.generativeai as genai
from dotenv import load_dotenv

from tools.logger import CustomException, logging

load_dotenv()


class Pdf_to_JSON:
    def __init__(self, tool_config):
        self.data_path = tool_config.get("data_path", r"./data/resumes")
        self.model = tool_config.get("model", "gemini-2.0-pro-exp-02-05")
        self.output_path = tool_config.get("output_path", r"./data/data.json")
        self.system_prompt = tool_config.get('system_prompt')
        self.generative_config = tool_config.get('generative_config')

    def __get_data(self):
        resumes = []

        for i, filename in enumerate(os.listdir(self.data_path)):
            if filename.lower().endswith(".pdf"):
                file_path = os.path.join(self.data_path, filename)
                doc = fitz.open(file_path)
                text = "".join(page.get_text("text") for page in doc)
                resumes.append(f"candidate{i}: {text}")
                doc.close()
        return "\n\n".join(resumes)

    def __save_json(self,data):
        match = re.search(r"```json\n(.*?)```", data, re.DOTALL)
        try:
            json_data = match.group(1).strip()
            with open(self.output_path, "w", encoding="utf-8") as json_file:
                json_file.write(json_data)
            logging.info(f"JSON data saved successfully at{self.output_path}")
        except Exception as e:
            logging.info("Error - No JSON data saved.")
            raise CustomException(e, sys)

    def generate(self):
        GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(self.model)
        input_text = Pdf_to_JSON.__get_data()
        combined_prompt = f"{self.system_prompt}\n\nUser Information:\n{input_text}"

        response = model.generate_content(
            combined_prompt, generation_config=self.generative_config
        )

        Pdf_to_JSON.__save_json(response.text)

