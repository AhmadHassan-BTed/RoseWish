import math

import pygame

from src.config.settings import settings
from src.entities.character import Character


class MrLover(Character):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, scale=5)
        self.holding_rose = False

    def draw(self, screen: pygame.Surface):
        pixel = self.scale
        x, y = int(self.x), int(self.y)
        breath_offset = 0
        if not self.walking:
            breath_offset = int(math.sin(self.anim_frame * 0.5) * 1)
        hair_positions = [
            (x, y),
            (x + pixel, y),
            (x + 2 * pixel, y),
            (x + 3 * pixel, y),
            (x + 4 * pixel, y),
            (x + 5 * pixel, y),
            (x, y + pixel),
            (x + 5 * pixel, y + pixel),
            (x, y + 2 * pixel),
            (x + 5 * pixel, y + 2 * pixel),
        ]
        for pos in hair_positions:
            pygame.draw.rect(screen, settings.BLACK, (pos[0], pos[1] + breath_offset, pixel, pixel))
        face_color = (255, 220, 190)
        face_positions = [
            (x + pixel, y + pixel),
            (x + 2 * pixel, y + pixel),
            (x + 3 * pixel, y + pixel),
            (x + 4 * pixel, y + pixel),
            (x + pixel, y + 2 * pixel),
            (x + 2 * pixel, y + 2 * pixel),
            (x + 3 * pixel, y + 2 * pixel),
            (x + 4 * pixel, y + 2 * pixel),
            (x + pixel, y + 3 * pixel),
            (x + 2 * pixel, y + 3 * pixel),
            (x + 3 * pixel, y + 3 * pixel),
            (x + 4 * pixel, y + 3 * pixel),
            (x + 2 * pixel, y + 4 * pixel),
            (x + 3 * pixel, y + 4 * pixel),
        ]
        for pos in face_positions:
            pygame.draw.rect(screen, face_color, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(
            screen,
            settings.BLACK,
            (
                x + pixel + pixel // 2,
                y + 2 * pixel + pixel // 2 + breath_offset,
                pixel // 2,
                pixel // 2,
            ),
        )
        pygame.draw.rect(
            screen,
            settings.WHITE,
            (
                x + pixel + pixel // 2 + pixel // 4,
                y + 2 * pixel + pixel // 2 + breath_offset,
                pixel // 4,
                pixel // 4,
            ),
        )
        pygame.draw.rect(
            screen,
            settings.BLACK,
            (
                x + 3 * pixel + pixel // 2,
                y + 2 * pixel + pixel // 2 + breath_offset,
                pixel // 2,
                pixel // 2,
            ),
        )
        pygame.draw.rect(
            screen,
            settings.WHITE,
            (
                x + 3 * pixel + pixel // 2 + pixel // 4,
                y + 2 * pixel + pixel // 2 + breath_offset,
                pixel // 4,
                pixel // 4,
            ),
        )
        smile_points = [
            (x + 2 * pixel, y + 3 * pixel + pixel // 2 + breath_offset),
            (x + 2 * pixel + pixel // 2, y + 3 * pixel + pixel + breath_offset),
            (x + 3 * pixel + pixel // 2, y + 3 * pixel + pixel + breath_offset),
            (x + 4 * pixel, y + 3 * pixel + pixel // 2 + breath_offset),
        ]
        pygame.draw.lines(screen, settings.DEEP_RED, False, smile_points, 2)
        pygame.draw.rect(
            screen, face_color, (x + 2 * pixel, y + 5 * pixel + breath_offset, pixel * 2, pixel)
        )
        shirt_color = (40, 60, 100)
        shirt_positions = [
            (x + pixel, y + 5 * pixel),
            (x + 2 * pixel, y + 5 * pixel),
            (x + 3 * pixel, y + 5 * pixel),
            (x + 4 * pixel, y + 5 * pixel),
            (x + pixel, y + 6 * pixel),
            (x + 2 * pixel, y + 6 * pixel),
            (x + 3 * pixel, y + 6 * pixel),
            (x + 4 * pixel, y + 6 * pixel),
            (x + pixel, y + 7 * pixel),
            (x + 2 * pixel, y + 7 * pixel),
            (x + 3 * pixel, y + 7 * pixel),
            (x + 4 * pixel, y + 7 * pixel),
            (x + 2 * pixel, y + 8 * pixel),
            (x + 3 * pixel, y + 8 * pixel),
        ]
        for pos in shirt_positions:
            pygame.draw.rect(screen, shirt_color, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(
            screen, settings.BLACK, (x + pixel, y + 9 * pixel + breath_offset, pixel * 2, pixel * 3)
        )
        pygame.draw.rect(
            screen,
            settings.BLACK,
            (x + 3 * pixel, y + 9 * pixel + breath_offset, pixel * 2, pixel * 3),
        )
        pygame.draw.rect(
            screen, (60, 40, 20), (x + pixel, y + 12 * pixel + breath_offset, pixel * 2, pixel)
        )
        pygame.draw.rect(
            screen, (60, 40, 20), (x + 3 * pixel, y + 12 * pixel + breath_offset, pixel * 2, pixel)
        )
        if self.holding_rose:
            rose_x = x + 6 * pixel if self.facing_right else x - 4 * pixel
            rose_y = y + 6 * pixel + breath_offset
            pygame.draw.rect(
                screen, (0, 120, 0), (rose_x + pixel // 2, rose_y, pixel // 2, pixel * 3)
            )
            pygame.draw.rect(screen, (0, 150, 0), (rose_x, rose_y + pixel, pixel, pixel // 2))
            pygame.draw.rect(
                screen, (0, 150, 0), (rose_x + pixel, rose_y + pixel * 2, pixel, pixel // 2)
            )
            petal_positions = [
                (rose_x, rose_y - pixel),
                (rose_x + pixel, rose_y - pixel),
                (rose_x - pixel // 2, rose_y - pixel // 2),
                (rose_x + pixel + pixel // 2, rose_y - pixel // 2),
                (rose_x + pixel // 2, rose_y - pixel - pixel // 2),
            ]
            for pos in petal_positions:
                pygame.draw.rect(screen, settings.ROSE_RED, (pos[0], pos[1], pixel, pixel))
            pygame.draw.rect(
                screen, settings.DEEP_RED, (rose_x + pixel // 2, rose_y - pixel // 2, pixel, pixel)
            )
