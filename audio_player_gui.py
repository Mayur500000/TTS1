# audio_player_gui.py
import pygame

def play_audio(audio_path):
    print("Current working directory:", pygame.get_cwd())
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # Example usage
    audio_file_path = "output_DSCC.mp3"  # Update with the actual output file path
    play_audio(audio_file_path)
