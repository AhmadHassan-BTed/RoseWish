import os
from pathlib import Path

from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Settings:
    # Game Settings
    WINDOW_TITLE = os.getenv("WINDOW_TITLE", "Rose Day Special")
    WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 1000))
    WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 700))
    FPS = int(os.getenv("FPS", 60))
    PIXEL_SIZE = 4

    # Character Names
    PLAYER_NAME = os.getenv("PLAYER_NAME", "Honey")
    PARTNER_NAME = os.getenv("PARTNER_NAME", "Sweetie")

    # Messages
    INTRO_MESSAGE = os.getenv("INTRO_MESSAGE", "A special day is dawning...")
    MEETING_MESSAGE = os.getenv("MEETING_MESSAGE", "Someone special is approaching...")
    PLAYER_GREETING = os.getenv("PLAYER_GREETING", "How are you, my love?")
    PARTNER_REPLY = os.getenv("PARTNER_REPLY", "I am wonderful, just a bit tired...")
    PLAYER_ADVICE = os.getenv(
        "PLAYER_ADVICE", "You've been working so hard. Rest your eyes for a moment..."
    )
    PARTNER_AGREE = os.getenv("PARTNER_AGREE", "You're right... I'll take a quick nap...")
    REVEAL_MESSAGE = os.getenv(
        "REVEAL_MESSAGE",
        "A rose for my most beautiful flower. I love you more than words can say. "
        "Happy Rose Day! ",
    )
    MARRIAGE_MESSAGE_1 = os.getenv("MARRIAGE_MESSAGE_1", "Happy Rose Day, my beautiful spouse.")
    MARRIAGE_MESSAGE_2 = os.getenv(
        "MARRIAGE_MESSAGE_2",
        "Thank you for making every day feel like a dream. "
        "May our love bloom forever like this rose.",
    )
    FINAL_MESSAGE = os.getenv(
        "FINAL_MESSAGE", "My heart, my soul, my everything...\nHappy Rose Day, My Love!"
    )

    # Assets
    MUSIC_PATH = str(BASE_DIR / os.getenv("MUSIC_PATH", "assets/music.mp3"))
    VOLUME = float(os.getenv("VOLUME", 0.5))

    # Titles
    MAIN_TITLE = os.getenv("MAIN_TITLE", "A Romantic Game")
    SUB_TITLE = os.getenv("SUB_TITLE", "A beautiful story")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (20, 20, 30)
    ROSE_RED = (220, 20, 60)
    DEEP_RED = (139, 0, 0)
    SOFT_PINK = (255, 182, 193)
    WINE_RED = (114, 47, 55)
    DREAMY_PINK = (255, 210, 220)
    HEART_RED = (255, 50, 80)
    STAR_YELLOW = (255, 255, 200)
    TREE_BROWN = (101, 67, 33)
    TREE_GREEN = (34, 139, 34)
    LIGHT_PURPLE = (216, 191, 216)


settings = Settings()
