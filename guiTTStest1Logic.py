#guiTTStest1Logic.py
import os
import pyttsx3
from PyPDF2 import PdfReader

class PDFConverterLogic:
    def __init__(self, pdf_paths):
        self.pdf_paths = pdf_paths
        self.pdf_index = 0

    def select_previous_pdf(self):
        self.pdf_index = (self.pdf_index - 1) % len(self.pdf_paths)
        return self.pdf_paths[self.pdf_index]

    def select_next_pdf(self):
        self.pdf_index = (self.pdf_index + 1) % len(self.pdf_paths)
        return self.pdf_paths[self.pdf_index]

    def convert_selected_pdf(self):
        selected_pdf = self.pdf_paths[self.pdf_index]
        output_path = f"output_{os.path.splitext(os.path.basename(selected_pdf))[0]}.mp3"

        text = self.extract_text_from_pdf(selected_pdf)
        self.generate_audiobook(text, output_path)

        return f"Audiobook generated for {os.path.basename(selected_pdf)} at {output_path}"

    def extract_text_from_pdf(self, pdf_path):
        text = ''
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page_num].extract_text()
        except Exception as e:
            return f"Error reading PDF: {e}"
        return text

    def generate_audiobook(self, text, output_path):
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()

    def get_selected_pdf(self):
        return self.pdf_paths[self.pdf_index]
