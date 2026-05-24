import pygame


class Character:
    def __init__(self, x: float, y: float, scale: int = 4):
        self.x = x
        self.y = y
        self.scale = scale
        self.anim_frame = 0
        self.anim_timer = 0.0
        self.facing_right = True
        self.walking = False

    def update(self, dt: float):
        self.anim_timer += dt
        if self.anim_timer > 0.2:
            self.anim_timer = 0.0
            if self.walking:
                self.anim_frame = (self.anim_frame + 1) % 4
            else:
                self.anim_frame = (self.anim_frame + 1) % 8

    def draw(self, screen: pygame.Surface):
        raise NotImplementedError("Subclasses must implement draw()")
