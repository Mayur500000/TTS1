# guiTTStest1Gui.py
import tkinter as tk
import os
import pyttsx3
from guiTTStest1Logic import PDFConverterLogic
from audio_player_gui import MP3PlayerGUI

class PDFToAudioConverterGUI:
    def __init__(self, master, pdf_paths, mp3_paths):
        self.master = master
        master.title("PDF to Audiobook Converter")
        master.bind("<Control-t>", self.switch_to_pdf_converter)
        master.bind("<Control-a>", self.switch_to_audio_player)
        master.bind("<Return>", self.convert_selected_pdf)
        master.bind("<Up>", self.select_previous_pdf)
        master.bind("<Down>", self.select_next_pdf)

        self.logic = PDFConverterLogic(pdf_paths)
        self.mp3_paths = mp3_paths

        self.pdf_label = tk.Label(master, text="")
        self.pdf_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.show_instructions()

    def show_instructions(self, event=None):
        instructions = (
            "Welcome to the PDF to Audiobook Converter!\n\n"
            "Use the arrow keys to navigate and press Enter to select a PDF.\n"
            "Press Ctrl+Q to quit the application.\n"
            "Press Ctrl+A to open the Audio Player."
        )

        self.speak(instructions)

        # Show additional message for Ctrl+A
        audio_instructions = "Press Ctrl+A to listen to the selected audio."
        self.speak(audio_instructions)

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

    def switch_to_audio_player(self, event=None):
    # Open the audio player as a child window
       audio_player_window = tk.Toplevel(self.master)
       print("MP3 Paths:", self.mp3_paths)  # Debugging line
       audio_player_app = MP3PlayerGUI(audio_player_window, self.mp3_paths)


    def switch_to_pdf_converter(self, event=None):
        # Close the audio player window
        for window in self.master.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()

if __name__ == "__main__":
    # Get the path to the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # List all files in the script's directory
    all_files = os.listdir(script_directory)

    # Filter only the files with the .pdf extension
    pdf_files = [file for file in all_files if file.endswith('.pdf')]

    # Create the pdf_paths list
    pdf_paths = [os.path.join(script_directory, pdf_file) for pdf_file in pdf_files]

    root = tk.Tk()
    app = PDFToAudioConverterGUI(root, pdf_paths, [])
    root.mainloop()
