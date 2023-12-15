import os
import pyttsx3
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ''
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def generate_audiobook_from_pdf(pdf_path, output_path='output1.mp3'):
    text = extract_text_from_pdf(pdf_path)
    engine = pyttsx3.init()
    engine.save_to_file(text, os.path.join('D:\\Mayur\\code\\TtS\\Tts1', output_path))
    engine.runAndWait()

# Example usage
pdf_file_path = 'D:/Mayur/code/TtS/TTS1/DSCC.pdf'
generate_audiobook_from_pdf(pdf_file_path)
