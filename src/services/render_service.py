from typing import List, Tuple

import pygame

from src.config.settings import settings


class RenderService:
    """
    Handles screen management and high-level drawing primitives.
    Provides a layer of abstraction over Pygame's surface operations.
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_TITLE)

    def fill(self, color: Tuple[int, int, int]):
        self.screen.fill(color)

    def draw_rect(
        self,
        color: Tuple[int, int, int],
        rect: Tuple[int, int, int, int],
        width: int = 0,
        border_radius: int = -1,
    ):
        pygame.draw.rect(self.screen, color, rect, width, border_radius)

    def draw_circle(
        self, color: Tuple[int, int, int], center: Tuple[int, int], radius: int, width: int = 0
    ):
        pygame.draw.circle(self.screen, color, center, radius, width)

    def draw_polygon(
        self, color: Tuple[int, int, int], points: List[Tuple[int, int]], width: int = 0
    ):
        pygame.draw.polygon(self.screen, color, points, width)

    def blit(self, source: pygame.Surface, dest: Tuple[int, int]):
        self.screen.blit(source, dest)

    def flip(self):
        pygame.display.flip()

    def get_screen(self) -> pygame.Surface:
        return self.screen
