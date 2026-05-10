import pygame
import random
import math
from typing import List, Dict
from src.config.settings import settings

class ThoughtManager:
    def __init__(self):
        self.thoughts: List[Dict] = []
        self.timer = 0.0

    def spawn_thought(self, x: float, y: float):
        thought_type = random.choice(['wolf', 'rose', 'noodles'])
        self.thoughts.append({
            'type': thought_type,
            'x': x + 30,
            'y': y - 60,
            'life': 5.0
        })

    def update(self, dt: float):
        for thought in self.thoughts[:]:
            thought['y'] -= 15 * dt
            thought['life'] -= dt
            thought['x'] += math.sin(thought['life'] * 2) * 0.5
            if thought['life'] <= 0:
                self.thoughts.remove(thought)

    def draw(self, screen: pygame.Surface):
        for thought in self.thoughts:
            self._draw_thought(screen, thought)

    def _draw_thought(self, screen: pygame.Surface, thought: Dict):
        x, y = int(thought['x']), int(thought['y'])
        bubble_radius = 25
        pygame.draw.circle(screen, settings.WHITE, (x, y), bubble_radius)
        pygame.draw.circle(screen, settings.ROSE_RED, (x, y), bubble_radius, 2)
        pygame.draw.circle(screen, settings.WHITE, (x - 15, y + 20), 8)
        pygame.draw.circle(screen, settings.ROSE_RED, (x - 15, y + 20), 8, 1)
        pygame.draw.circle(screen, settings.WHITE, (x - 25, y + 30), 5)
        pygame.draw.circle(screen, settings.ROSE_RED, (x - 25, y + 30), 5, 1)
        
        if thought['type'] == 'wolf':
            wolf_points = [
                (x - 10, y + 5), (x - 8, y - 5), (x - 5, y - 8),
                (x, y - 10), (x + 5, y - 8), (x + 8, y - 5),
                (x + 10, y + 5), (x + 5, y + 8), (x - 5, y + 8)
            ]
            pygame.draw.polygon(screen, (80, 80, 80), wolf_points)
            pygame.draw.circle(screen, settings.STAR_YELLOW, (x - 3, y - 2), 2)
            pygame.draw.circle(screen, settings.STAR_YELLOW, (x + 3, y - 2), 2)
        elif thought['type'] == 'rose':
            pygame.draw.rect(screen, (0, 120, 0), (x - 1, y + 2, 2, 12))
            leaf_points_left = [(x - 5, y + 6), (x - 1, y + 7), (x - 1, y + 10)]
            leaf_points_right = [(x + 5, y + 9), (x + 1, y + 10), (x + 1, y + 13)]
            pygame.draw.polygon(screen, (0, 150, 0), leaf_points_left)
            pygame.draw.polygon(screen, (0, 150, 0), leaf_points_right)
            for i in range(5):
                angle = i * (2 * math.pi / 5)
                petal_x = x + math.cos(angle) * 6
                petal_y = y - 5 + math.sin(angle) * 6
                pygame.draw.circle(screen, settings.ROSE_RED, (int(petal_x), int(petal_y)), 4)
            pygame.draw.circle(screen, settings.DEEP_RED, (x, y - 5), 3)
        elif thought['type'] == 'noodles':
            bowl_rect = pygame.Rect(x - 10, y + 2, 20, 12)
            pygame.draw.ellipse(screen, (200, 150, 100), bowl_rect)
            pygame.draw.ellipse(screen, (180, 130, 80), bowl_rect, 2)
            for i in range(4):
                start_x = x - 8 + i * 4
                points = [(start_x, y - 5), (start_x + 1, y - 3), (start_x, y - 1), (start_x + 1, y + 1)]
                pygame.draw.lines(screen, (255, 220, 150), False, points, 2)
            pygame.draw.line(screen, (100, 60, 30), (x + 5, y - 8), (x + 12, y - 12), 2)
            pygame.draw.line(screen, (100, 60, 30), (x + 7, y - 8), (x + 14, y - 12), 2)
