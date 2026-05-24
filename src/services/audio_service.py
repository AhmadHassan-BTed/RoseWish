import pygame

from src.config.settings import settings


class AudioService:
    def __init__(self):
        # Initializing with specific parameters from original source for stability
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

    def play_music(self, file_path: str, loop: int = -1):
        try:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.set_volume(settings.VOLUME)
                pygame.mixer.music.play(loop)
        except pygame.error as e:
            print(f"Audio Error: {e}")

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume: float):
        pygame.mixer.music.set_volume(volume)
