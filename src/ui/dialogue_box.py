import pygame
from src.config.settings import settings

class DialogueBox:
    def __init__(self):
        self.active = False
        self.message = ""
        self.speaker = ""
        self.timer = 0.0
        self.font_name = pygame.font.Font(None, 32)
        self.font_msg = pygame.font.Font(None, 28)

    def show(self, speaker: str, message: str, duration: float = 3.0):
        self.active = True
        self.speaker = speaker
        self.message = message
        self.timer = duration

    def update(self, dt: float):
        if self.active:
            self.timer -= dt
            if self.timer <= 0:
                self.active = False

    def draw(self, screen: pygame.Surface):
        if not self.active:
            return
        box_width = 600
        box_height = 120
        box_x = (settings.WINDOW_WIDTH - box_width) // 2
        box_y = settings.WINDOW_HEIGHT - box_height - 20
        
        # Box background and border
        pygame.draw.rect(screen, settings.WHITE, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, settings.ROSE_RED, (box_x, box_y, box_width, box_height), 4)
        
        # Speaker name
        name_text = self.font_name.render(self.speaker, True, settings.WINE_RED)
        screen.blit(name_text, (box_x + 20, box_y + 10))
        
        # Message with wrapping
        words = self.message.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if self.font_msg.size(test_line)[0] < box_width - 40:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        
        y_offset = box_y + 45
        for line in lines[:2]:  # Limit to 2 lines as in original
            msg_text = self.font_msg.render(line.strip(), True, settings.BLACK)
            screen.blit(msg_text, (box_x + 20, y_offset))
            y_offset += 30
