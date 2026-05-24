import math
import random
from dataclasses import dataclass
from typing import List, Tuple

import pygame

from src.config.settings import settings


@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: float
    max_life: float
    color: Tuple[int, int, int]
    size: int
    particle_type: str = "snow"


class ParticleManager:
    def __init__(self):
        self.particles: List[Particle] = []

    def spawn_snow(self):
        self.particles.append(
            Particle(
                x=random.randint(0, settings.WINDOW_WIDTH),
                y=-10,
                vx=random.uniform(-15, 15),
                vy=random.uniform(30, 70),
                life=random.uniform(10, 15),
                max_life=15,
                color=settings.WHITE,
                size=random.randint(2, 5),
                particle_type="snow",
            )
        )

    def spawn_rose_petal(self):
        self.particles.append(
            Particle(
                x=random.randint(0, settings.WINDOW_WIDTH),
                y=-10,
                vx=random.uniform(-25, 25),
                vy=random.uniform(10, 30),
                life=random.uniform(8, 12),
                max_life=12,
                color=random.choice([settings.ROSE_RED, settings.SOFT_PINK, settings.DEEP_RED]),
                size=random.randint(4, 8),
                particle_type="rose_petal",
            )
        )

    def spawn_heart(self, x: float, y: float):
        self.particles.append(
            Particle(
                x=x + random.uniform(-20, 20),
                y=y,
                vx=random.uniform(-20, 20),
                vy=random.uniform(-100, -40),
                life=random.uniform(2.5, 4.5),
                max_life=4.5,
                color=settings.HEART_RED,
                size=random.randint(6, 10),
                particle_type="heart",
            )
        )

    def spawn_dream_particle(self):
        self.particles.append(
            Particle(
                x=random.randint(0, settings.WINDOW_WIDTH),
                y=random.randint(0, settings.WINDOW_HEIGHT),
                vx=random.uniform(-15, 15),
                vy=random.uniform(-15, 15),
                life=random.uniform(4, 8),
                max_life=8,
                color=random.choice(
                    [settings.DREAMY_PINK, settings.LIGHT_PURPLE, settings.SOFT_PINK]
                ),
                size=random.randint(4, 10),
                particle_type="dream",
            )
        )

    def spawn_sparkle(self, x: float, y: float):
        self.particles.append(
            Particle(
                x=x,
                y=y,
                vx=random.uniform(-10, 10),
                vy=random.uniform(-10, 10),
                life=random.uniform(0.5, 1.5),
                max_life=1.5,
                color=settings.STAR_YELLOW,
                size=random.randint(2, 4),
                particle_type="sparkle",
            )
        )

    def update(self, dt: float):
        for particle in self.particles[:]:
            if particle.particle_type in ["rose_petal", "heart"]:
                particle.vy += 50 * dt
            particle.x += particle.vx * dt
            particle.y += particle.vy * dt
            particle.life -= dt
            if particle.life <= 0:
                self.particles.remove(particle)

    def draw(self, screen: pygame.Surface, foreground: bool = True):
        for particle in self.particles:
            is_foreground = particle.particle_type not in ["snow", "rose_petal"]
            if is_foreground == foreground:
                self._draw_particle(screen, particle)

    def _draw_particle(self, screen, particle):
        alpha_ratio = particle.life / particle.max_life
        if particle.particle_type == "heart":
            self._draw_heart(
                screen, particle.x, particle.y, particle.size, particle.color, alpha_ratio
            )
        elif particle.particle_type == "sparkle":
            size = int(particle.size * alpha_ratio)
            self._draw_star(screen, particle.x, particle.y, size, particle.color)
        elif particle.particle_type == "rose_petal":
            size = particle.size
            angle = particle.life * 2
            for i in range(3):
                offset_x = math.cos(angle + i * 2) * size
                offset_y = math.sin(angle + i * 2) * size
                pygame.draw.circle(
                    screen,
                    particle.color,
                    (int(particle.x + offset_x), int(particle.y + offset_y)),
                    size // 2,
                )
        else:
            size = int(particle.size * alpha_ratio) if alpha_ratio < 1 else particle.size
            pygame.draw.circle(
                screen, particle.color, (int(particle.x), int(particle.y)), max(1, size)
            )

    def _draw_heart(self, screen, x, y, size, color, alpha):
        s = max(1, int(size // 2 * alpha))
        positions = [
            (x - s, y),
            (x + s, y),
            (x - 2 * s, y + s),
            (x - s, y + s),
            (x, y + s),
            (x + s, y + s),
            (x + 2 * s, y + s),
            (x - 2 * s, y + 2 * s),
            (x - s, y + 2 * s),
            (x, y + 2 * s),
            (x + s, y + 2 * s),
            (x + 2 * s, y + 2 * s),
            (x - s, y + 3 * s),
            (x, y + 3 * s),
            (x + s, y + 3 * s),
            (x, y + 4 * s),
        ]
        for px, py in positions:
            pygame.draw.rect(screen, color, (int(px), int(py), s, s))

    def _draw_star(self, screen, x, y, size, color):
        points = [
            (x, y - size),
            (x - size // 3, y - size // 3),
            (x - size, y),
            (x - size // 3, y + size // 3),
            (x, y + size),
            (x + size // 3, y + size // 3),
            (x + size, y),
            (x + size // 3, y - size // 3),
        ]
        pygame.draw.polygon(screen, color, points)
