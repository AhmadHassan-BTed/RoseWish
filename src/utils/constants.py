from enum import Enum

class GameState(Enum):
    TITLE = "title"
    INTRO = "intro"
    WANDER = "wander"
    MEETING = "meeting"
    CONVERSATION = "conversation"
    SLEEP_TRANSITION = "sleep_transition"
    SLEEP = "sleep"
    DREAM = "dream"
    WAKE_TRANSITION = "wake_transition"
    REVEAL = "reveal"
    KISS = "kiss"
    MARRIAGE = "marriage"
    END = "end"
