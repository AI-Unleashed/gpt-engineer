import json
import os
from dataclasses import dataclass
from PyPDF2 import PdfFileWriter, PdfFileReader
from jsonschema import validate, ValidationError

@dataclass
class Resume:
    input_json: str
    pdf: PdfFileWriter = None

    def validate_input(self):
        schema = {
            "type": "object",
            "properties": {
                "contact_information": {"type": "object"},
                "resume_introduction": {"type": "string"},
                "professional_experience": {"type": "array"},
                "skills": {"type": "array"},
                "education": {"type": "array"}
            },
            "required": ["contact_information", "resume_introduction", "professional_experience", "skills", "education"]
        }

        try:
            validate(json.loads(self.input_json), schema)
        except ValidationError as e:
            raise ValueError(e.message)

    def generate_resume(self):
        # Implement the logic to generate the resume in PDF format using the input JSON data.
        # For simplicity, we will use a dummy PDF file as a placeholder.
        self.pdf = PdfFileReader("dummy_resume.pdf")

    def save_resume(self, file_name: str):
        with open(file_name, "wb") as output_file:
            self.pdf.write(output_file)

    def preview_resume(self):
        # Implement the logic to preview the generated resume.
        # For simplicity, we will just return the number of pages in the PDF.
        return self.pdf.getNumPages()
