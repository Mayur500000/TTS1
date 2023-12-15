# guiTTStest1Gui.py
import tkinter as tk
import os
import pyttsx3
from guiTTStest1Logic import PDFConverterLogic

class PDFToAudioConverterGUI:
    def __init__(self, master, pdf_paths):
        self.master = master
        master.title("PDF to Audiobook Converter")
        master.bind("<Control-t>", self.show_instructions)
        master.bind("<Return>", self.convert_selected_pdf)
        master.bind("<Up>", self.select_previous_pdf)
        master.bind("<Down>", self.select_next_pdf)

        self.logic = PDFConverterLogic(pdf_paths)

        self.pdf_label = tk.Label(master, text="")
        self.pdf_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.show_instructions()

    def show_instructions(self, event=None):
        instructions = (
            "Welcome to the PDF to Audiobook Converter!\n\n"
            "Use the arrow keys to navigate and press Enter to select a PDF.\n"
            "Press Ctrl+Q to quit the application."
        )

        self.speak(instructions)

        self.show_pdf_selection()

    def show_pdf_selection(self):
        selected_pdf = self.logic.get_selected_pdf()
        message = f"Selected PDF: {os.path.basename(selected_pdf)}"
        self.pdf_label.config(text=message)
        self.speak(message)

    def select_previous_pdf(self, event=None):
        self.logic.select_previous_pdf()
        self.show_pdf_selection()

    def select_next_pdf(self, event=None):
        self.logic.select_next_pdf()
        self.show_pdf_selection()

    def convert_selected_pdf(self, event=None):
        result_message = self.logic.convert_selected_pdf()
        self.speak(result_message)
        self.show_pdf_selection()

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    pdf_paths = [
        'D:/Mayur/code/TtS/TTS1/DSCC.pdf',
        'D:/Mayur/code/TtS/TTS1/test1.pdf',
        'D:/Mayur/code/TtS/TTS1/EH.pdf'
    ]
    app = PDFToAudioConverterGUI(root, pdf_paths)
    root.mainloop()
