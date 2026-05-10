import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

class Settings:
    # Game Settings
    WINDOW_TITLE = os.getenv("WINDOW_TITLE", "Beenie kay liyeee Gameeee")
    WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 1000))
    WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 700))
    FPS = int(os.getenv("FPS", 60))
    PIXEL_SIZE = 4

    # Character Names
    PLAYER_NAME = os.getenv("PLAYER_NAME", "Ahmad")
    PARTNER_NAME = os.getenv("PARTNER_NAME", "Beenie")

    # Messages (Original Urdu/English mix)
    INTRO_MESSAGE = os.getenv("INTRO_MESSAGE", "Kal ka din....")
    MEETING_MESSAGE = os.getenv("MEETING_MESSAGE", "waohhh.....koi a rha hayyyy....")
    PLAYER_GREETING = os.getenv("PLAYER_GREETING", "Kesi hain meri pyari jaaannnn...")
    PARTNER_REPLY = os.getenv("PARTNER_REPLY", "Theak hun.....")
    PLAYER_ADVICE = os.getenv("PLAYER_ADVICE", "Aryyy, sirif theak, ap to itii thaki thaki lag rahi hain, thoru sa so jayen naww...")
    PARTNER_AGREE = os.getenv("PARTNER_AGREE", "ohhh....okieeee...")
    REVEAL_MESSAGE = os.getenv("REVEAL_MESSAGE", "Yae Phul, meri Rosey kay liye, Meri Ghulabo kay liye... I love you, meri pyari jaan. Happy Rose Day! 🌹")
    MARRIAGE_MESSAGE_1 = os.getenv("MARRIAGE_MESSAGE_1", "Happy Rose Day, Beenie Beghum")
    MARRIAGE_MESSAGE_2 = os.getenv("MARRIAGE_MESSAGE_2", "Thenkeww for being my roseyy, or red red apki cheeks and nosey. Allah talla meri pyar beghum ki cheeks ko asy hi hasta muskurata and rose red rakhy")
    FINAL_MESSAGE = os.getenv("FINAL_MESSAGE", "Me rasgulla, my roseie, meri golgappa, My Shamooo...MUUAAHHH. \nHappy Rose Day Meri Pyari Beghum")

    # Assets
    MUSIC_PATH = str(BASE_DIR / os.getenv("MUSIC_PATH", "assets/music.mp3"))
    VOLUME = float(os.getenv("VOLUME", 0.5))

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
