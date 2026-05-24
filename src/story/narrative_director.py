from dataclasses import dataclass
from typing import List

from src.config.settings import settings
from src.core.event_bus import event_bus


@dataclass
class DialogueLine:
    speaker: str
    text: str
    duration: float


class NarrativeDirector:
    """
    Manages the story progression independently of game systems.
    Communicates via the EventBus to trigger UI and animations.
    """

    def __init__(self):
        self.current_state = "START"
        self.timer = 0
        self.dialogue_queue: List[DialogueLine] = []

    def load_story_beat(self, state: str):
        self.current_state = state
        self.timer = 0
        # This could load from a JSON file in a more complex app
        if state == "MEETING":
            self.dialogue_queue = [
                DialogueLine(settings.PLAYER_NAME, settings.PLAYER_GREETING, 4.0),
                DialogueLine(settings.PARTNER_NAME, settings.PARTNER_REPLY, 4.0),
                DialogueLine(settings.PLAYER_NAME, settings.PLAYER_ADVICE, 4.0),
                DialogueLine(settings.PARTNER_NAME, settings.PARTNER_AGREE, 3.0),
            ]

    def update(self, dt: float):
        if self.dialogue_queue:
            self.timer -= dt
            if self.timer <= 0:
                line = self.dialogue_queue.pop(0)
                self.timer = line.duration
                event_bus.emit(
                    "DIALOGUE_TRIGGERED",
                    speaker=line.speaker,
                    message=line.text,
                    duration=line.duration,
                )
