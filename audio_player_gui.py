#audio_player_gui.py
import os
import tkinter as tk
import pyttsx3

class MP3PlayerLogic:
    def __init__(self, mp3_paths):
        self.mp3_paths = mp3_paths
        self.selected_index = 0

    def get_selected_mp3(self):
        return self.mp3_paths[self.selected_index]

    def select_previous_mp3(self):
        if self.selected_index > 0:
            self.selected_index -= 1

    def select_next_mp3(self):
        if self.selected_index < len(self.mp3_paths) - 1:
            self.selected_index += 1

    def play_selected_mp3(self):
        selected_mp3 = self.get_selected_mp3()
        return f"Now playing: {os.path.basename(selected_mp3)}"

class MP3PlayerGUI:
    def __init__(self, master, mp3_paths):
        self.master = master
        master.title("MP3 Player")
        master.bind("<Control-t>", self.show_instructions)
        master.bind("<Return>", self.play_selected_mp3)
        master.bind("<Up>", self.select_previous_mp3)
        master.bind("<Down>", self.select_next_mp3)

        self.logic = MP3PlayerLogic(mp3_paths)

        self.mp3_label = tk.Label(master, text="")
        self.mp3_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.show_instructions()

    def show_instructions(self, event=None):
        instructions = (
            "Welcome to the MP3 Player!\n\n"
            "Use the arrow keys to navigate and press Enter to play an MP3 file.\n"
            "Press Ctrl+Q to quit the application."
        )

        self.speak(instructions)

        self.show_mp3_selection()

    def show_mp3_selection(self):
        selected_mp3 = self.logic.get_selected_mp3()
        message = f"Selected MP3: {os.path.basename(selected_mp3)}"
        self.mp3_label.config(text=message)
        self.speak(message)

    def select_previous_mp3(self, event=None):
        self.logic.select_previous_mp3()
        self.show_mp3_selection()

    def select_next_mp3(self, event=None):
        self.logic.select_next_mp3()
        self.show_mp3_selection()

    def play_selected_mp3(self, event=None):
        result_message = self.logic.play_selected_mp3()
        self.speak(result_message)
        self.show_mp3_selection()

        # Open the MP3 file with the default media player
        os.startfile(self.logic.get_selected_mp3())

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    # Get the path to the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # List all files in the script's directory
    all_files = os.listdir(script_directory)

    # Filter only the files with the .mp3 extension
    mp3_files = [file for file in all_files if file.endswith('.mp3')]

    # Create the mp3_paths list
    mp3_paths = [os.path.join(script_directory, mp3_file) for mp3_file in mp3_files]

    root = tk.Tk()
    app = MP3PlayerGUI(root, mp3_paths)
    root.mainloop()