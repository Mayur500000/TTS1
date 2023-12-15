from gtts import gTTS
import os
from gtts_token import gtts_token
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

def generate_audiobook_from_pdf(pdf_path, language='en', voice_speed=1.0, output_path='output.mp3'):
    text = extract_text_from_pdf(pdf_path)
    token = gtts_token.Token(language)
    tts = gTTS(text=text, lang=language, slow=False, tld='com', token=token.calculate_token(text))
    output_file_path = os.path.join('D:\\Mayur\\code\\TtS\\Tts1', output_path)
    tts.save(output_file_path)

# Example usage
pdf_file_path = 'D:/Mayur/code/TtS/TTS1/test1.pdf'
generate_audiobook_from_pdf(pdf_file_path, language='en', voice_speed=1.5)
