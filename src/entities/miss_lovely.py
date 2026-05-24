import math

import pygame

from src.config.settings import settings
from src.entities.character import Character


class MissLovely(Character):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, scale=5)
        self.sleeping = False
        self.sleep_timer = 0.0
        self.awake = True

    def draw(self, screen: pygame.Surface):
        pixel = self.scale
        x, y = int(self.x), int(self.y)
        if self.sleeping:
            self.draw_sleeping(screen, x, y, pixel)
        else:
            self.draw_standing(screen, x, y, pixel)

    def draw_standing(self, screen: pygame.Surface, x: int, y: int, pixel: int):
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
            (x + pixel, y + pixel),
            (x + 4 * pixel, y + pixel),
            (x + 5 * pixel, y + pixel),
            (x, y + 2 * pixel),
            (x + 5 * pixel, y + 2 * pixel),
        ]
        for pos in hair_positions:
            pygame.draw.rect(screen, settings.BLACK, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(screen, settings.ROSE_RED, (x + 5 * pixel, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, settings.ROSE_RED, (x + 6 * pixel, y + pixel, pixel // 2, pixel))
        face_color = (255, 220, 200)
        face_positions = [
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
        blink = self.anim_frame == 7
        if not blink:
            pygame.draw.rect(
                screen,
                settings.BLACK,
                (
                    x + pixel + pixel // 3,
                    y + 2 * pixel + pixel // 2 + breath_offset,
                    pixel // 2,
                    pixel // 2,
                ),
            )
            pygame.draw.rect(
                screen,
                settings.WHITE,
                (
                    x + pixel + pixel // 2,
                    y + 2 * pixel + pixel // 2 + breath_offset,
                    pixel // 4,
                    pixel // 4,
                ),
            )
            pygame.draw.rect(
                screen,
                settings.BLACK,
                (
                    x + 3 * pixel + pixel // 3,
                    y + 2 * pixel + pixel // 2 + breath_offset,
                    pixel // 2,
                    pixel // 2,
                ),
            )
            pygame.draw.rect(
                screen,
                settings.WHITE,
                (
                    x + 3 * pixel + pixel // 2,
                    y + 2 * pixel + pixel // 2 + breath_offset,
                    pixel // 4,
                    pixel // 4,
                ),
            )
        else:
            pygame.draw.line(
                screen,
                settings.BLACK,
                (x + pixel, y + 2 * pixel + pixel // 2 + breath_offset),
                (x + 2 * pixel - pixel // 2, y + 2 * pixel + pixel // 2 + breath_offset),
                2,
            )
            pygame.draw.line(
                screen,
                settings.BLACK,
                (x + 3 * pixel, y + 2 * pixel + pixel // 2 + breath_offset),
                (x + 4 * pixel - pixel // 2, y + 2 * pixel + pixel // 2 + breath_offset),
                2,
            )
        pygame.draw.rect(
            screen,
            settings.SOFT_PINK,
            (x + pixel // 2, y + 3 * pixel + breath_offset, pixel, pixel // 2),
        )
        pygame.draw.rect(
            screen,
            settings.SOFT_PINK,
            (x + 4 * pixel + pixel // 2, y + 3 * pixel + breath_offset, pixel, pixel // 2),
        )
        smile_points = [
            (x + 2 * pixel, y + 3 * pixel + pixel // 2 + breath_offset),
            (x + 2 * pixel + pixel // 2, y + 3 * pixel + pixel - pixel // 4 + breath_offset),
            (x + 3 * pixel + pixel // 2, y + 3 * pixel + pixel - pixel // 4 + breath_offset),
            (x + 4 * pixel, y + 3 * pixel + pixel // 2 + breath_offset),
        ]
        pygame.draw.lines(screen, settings.DEEP_RED, False, smile_points, 2)
        pygame.draw.rect(
            screen, face_color, (x + 2 * pixel, y + 5 * pixel + breath_offset, pixel * 2, pixel)
        )
        dress_positions = [
            (x + pixel, y + 5 * pixel),
            (x + 2 * pixel, y + 5 * pixel),
            (x + 3 * pixel, y + 5 * pixel),
            (x + 4 * pixel, y + 5 * pixel),
            (x + pixel, y + 6 * pixel),
            (x + 2 * pixel, y + 6 * pixel),
            (x + 3 * pixel, y + 6 * pixel),
            (x + 4 * pixel, y + 6 * pixel),
            (x, y + 7 * pixel),
            (x + pixel, y + 7 * pixel),
            (x + 2 * pixel, y + 7 * pixel),
            (x + 3 * pixel, y + 7 * pixel),
            (x + 4 * pixel, y + 7 * pixel),
            (x + 5 * pixel, y + 7 * pixel),
            (x, y + 8 * pixel),
            (x + pixel, y + 8 * pixel),
            (x + 2 * pixel, y + 8 * pixel),
            (x + 3 * pixel, y + 8 * pixel),
            (x + 4 * pixel, y + 8 * pixel),
            (x + 5 * pixel, y + 8 * pixel),
            (x + 6 * pixel, y + 8 * pixel),
            (x, y + 9 * pixel),
            (x + pixel, y + 9 * pixel),
            (x + 2 * pixel, y + 9 * pixel),
            (x + 3 * pixel, y + 9 * pixel),
            (x + 4 * pixel, y + 9 * pixel),
            (x + 5 * pixel, y + 9 * pixel),
            (x + 6 * pixel, y + 9 * pixel),
        ]
        for pos in dress_positions:
            pygame.draw.rect(
                screen, settings.ROSE_RED, (pos[0], pos[1] + breath_offset, pixel, pixel)
            )
        highlight_color = (255, 100, 120)
        pygame.draw.rect(
            screen, highlight_color, (x + 2 * pixel, y + 6 * pixel + breath_offset, pixel, pixel)
        )
        if self.walking and self.anim_frame % 2 == 0:
            pygame.draw.rect(
                screen, face_color, (x + pixel, y + 10 * pixel + breath_offset, pixel, pixel * 2)
            )
            pygame.draw.rect(
                screen,
                face_color,
                (x + 4 * pixel, y + 10 * pixel + pixel + breath_offset, pixel, pixel),
            )
        else:
            pygame.draw.rect(
                screen,
                face_color,
                (x + 2 * pixel, y + 10 * pixel + breath_offset, pixel, pixel * 2),
            )
            pygame.draw.rect(
                screen,
                face_color,
                (x + 3 * pixel, y + 10 * pixel + breath_offset, pixel, pixel * 2),
            )

    def draw_sleeping(self, screen: pygame.Surface, x: int, y: int, pixel: int):
        ground_y = y + (6 * pixel)
        pygame.draw.rect(screen, settings.BLACK, (x, ground_y, 4 * pixel, 4 * pixel))
        face_color = (255, 220, 200)
        pygame.draw.rect(
            screen, face_color, (x + 1 * pixel, ground_y + 1 * pixel, 3 * pixel, 3 * pixel)
        )
        pygame.draw.rect(screen, settings.BLACK, (x + 2 * pixel, ground_y + 2 * pixel, pixel, 1))
        pygame.draw.rect(
            screen, settings.ROSE_RED, (x + 4 * pixel, ground_y + 1 * pixel, 5 * pixel, 3 * pixel)
        )
        pygame.draw.rect(
            screen, settings.ROSE_RED, (x + 4 * pixel, ground_y + 1 * pixel, pixel, pixel)
        )
        pygame.draw.rect(
            screen, face_color, (x + 9 * pixel, ground_y + 2 * pixel, 1 * pixel, 2 * pixel)
        )
        current_time = pygame.time.get_ticks()
        if (current_time // 600) % 2 == 0:
            font = pygame.font.Font(None, 24)
            z_surf = font.render("Z", True, settings.WINE_RED)
            screen.blit(z_surf, (x + 2 * pixel, ground_y - 20))
            if (current_time // 300) % 2 == 0:
                z_small = font.render("z", True, settings.WINE_RED)
                screen.blit(z_small, (x + 4 * pixel, ground_y - 35))
