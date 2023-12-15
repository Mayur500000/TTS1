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

def generate_audiobook_from_pdf(pdf_path, output_path='output1.mp3', language='hi'):
    text = extract_text_from_pdf(pdf_path)
    
    # Initialize text-to-speech engine with Hindi language setting
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # You can adjust the speech rate as needed
    engine.setProperty('voice', f'{language}')
    
    try:
        # Save the speech to the specified output path
        engine.save_to_file(text, os.path.join('D:\\Mayur\\code\\TtS\\Tts1', output_path))
        engine.runAndWait()
    except Exception as e:
        print(f"Error generating audiobook: {e}")

# Example usage with Hindi language selection (language='hi')
pdf_file_path = 'D:/Mayur/code/TtS/TTS1/test1.pdf'
generate_audiobook_from_pdf(pdf_file_path, language='hi')
