import pygame
import math
import random
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum
import io
import base64
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60
PIXEL_SIZE = 4  
WHITE = (255, 255, 255)
SNOW_WHITE = (250, 250, 255)
DEEP_RED = (139, 0, 0)
ROSE_RED = (220, 20, 60)
SOFT_PINK = (255, 182, 193)
WINE_RED = (114, 47, 55)
BLACK = (20, 20, 30)
DREAMY_PINK = (255, 210, 220)
HEART_RED = (255, 50, 80)
SKY_BLUE = (135, 206, 250)
DARK_BLUE = (25, 25, 112)
LIGHT_PURPLE = (216, 191, 216)
DARK_PURPLE = (75, 0, 130)
TREE_BROWN = (101, 67, 33)
TREE_GREEN = (34, 139, 34)
GRASS_GREEN = (124, 252, 0)
NIGHT_SKY = (15, 15, 40)
STAR_YELLOW = (255, 255, 200)
STATE_TITLE = "title"
STATE_INTRO = "intro"
STATE_WANDER = "wander"
STATE_MEETING = "meeting"
STATE_CONVERSATION = "conversation"
STATE_SLEEP_TRANSITION = "sleep_transition"
STATE_SLEEP = "sleep"
STATE_DREAM = "dream"
STATE_WAKE_TRANSITION = "wake_transition"
STATE_REVEAL = "reveal"
STATE_KISS = "kiss"
STATE_MARRIAGE = "marriage"
STATE_END = "end"
def create_day_background():
    surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    for y in range(WINDOW_HEIGHT):
        ratio = y / WINDOW_HEIGHT
        r = int(135 * (1 - ratio) + 200 * ratio)
        g = int(206 * (1 - ratio) + 230 * ratio)
        b = int(250 * (1 - ratio) + 255 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WINDOW_WIDTH, y))
    pygame.draw.circle(surface, (255, 255, 200), (850, 120), 60)
    pygame.draw.circle(surface, (255, 255, 150), (850, 120), 50)
    for i in range(12):
        angle = i * (math.pi * 2 / 12)
        start_x = 850 + math.cos(angle) * 70
        start_y = 120 + math.sin(angle) * 70
        end_x = 850 + math.cos(angle) * 100
        end_y = 120 + math.sin(angle) * 100
        pygame.draw.line(surface, (255, 255, 180), (start_x, start_y), (end_x, end_y), 3)
    cloud_positions = [(200, 100), (500, 150), (750, 80), (300, 200)]
    for cx, cy in cloud_positions:
        pygame.draw.ellipse(surface, (255, 255, 255), (cx, cy, 120, 40))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 20, cy - 15, 80, 50))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 60, cy - 10, 70, 45))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 80, cy, 90, 35))
    mountain_points = [
        (0, 400), (150, 300), (300, 350), (450, 280), (600, 320), (750, 260), (900, 300), (1000, 350), (1000, 700), (0, 700)
    ]
    pygame.draw.polygon(surface, (150, 180, 150), mountain_points)
    shadow_points = [
        (150, 300), (300, 350), (300, 700), (150, 700)
    ]
    pygame.draw.polygon(surface, (130, 160, 130), shadow_points)
    shadow_points2 = [
        (600, 320), (750, 260), (750, 700), (600, 700)
    ]
    pygame.draw.polygon(surface, (130, 160, 130), shadow_points2)
    pygame.draw.rect(surface, (144, 238, 144), (0, WINDOW_HEIGHT - 150, WINDOW_WIDTH, 150))
    for i in range(0, WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        grass_shade = random.randint(100, 180)
        pygame.draw.line(surface, (grass_shade, 200, grass_shade),
                        (i, WINDOW_HEIGHT - 150),
                        (i, WINDOW_HEIGHT - 150 + grass_height), 2)
    flower_colors = [(255, 100, 150), (255, 150, 200), (255, 200, 100), (200, 150, 255)]
    for _ in range(30):
        fx = random.randint(50, WINDOW_WIDTH - 50)
        fy = random.randint(WINDOW_HEIGHT - 140, WINDOW_HEIGHT - 50)
        flower_color = random.choice(flower_colors)
        pygame.draw.line(surface, (0, 150, 0), (fx, fy), (fx, fy + 15), 2)
        for j in range(5):
            angle = j * (2 * math.pi / 5)
            petal_x = fx + math.cos(angle) * 5
            petal_y = fy + math.sin(angle) * 5
            pygame.draw.circle(surface, flower_color, (int(petal_x), int(petal_y)), 3)
        pygame.draw.circle(surface, (255, 200, 0), (fx, fy), 2)
    tree_positions = [(100, WINDOW_HEIGHT - 150), (300, WINDOW_HEIGHT - 150), 
                      (700, WINDOW_HEIGHT - 150), (900, WINDOW_HEIGHT - 150)]
    for tx, ty in tree_positions:
        pygame.draw.rect(surface, (101, 67, 33), (tx - 15, ty - 80, 30, 80))
        for i in range(5):
            offset_x = random.randint(-30, 30)
            offset_y = random.randint(-40, -20)
            pygame.draw.circle(surface, (34, 139, 34), (tx + offset_x, ty - 60 + offset_y), 25)
        pygame.draw.circle(surface, (44, 160, 44), (tx, ty - 70), 30)
        pygame.draw.circle(surface, (54, 180, 54), (tx - 15, ty - 60), 25)
        pygame.draw.circle(surface, (54, 180, 54), (tx + 15, ty - 60), 25)
    return surface
def create_night_background():
    surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    for y in range(WINDOW_HEIGHT):
        ratio = y / WINDOW_HEIGHT
        r = int(15 * (1 - ratio) + 30 * ratio)
        g = int(15 * (1 - ratio) + 25 * ratio)
        b = int(40 * (1 - ratio) + 60 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WINDOW_WIDTH, y))
    for _ in range(200):
        sx = random.randint(0, WINDOW_WIDTH)
        sy = random.randint(0, WINDOW_HEIGHT // 2)
        brightness = random.randint(150, 255)
        size = random.choice([1, 1, 1, 2, 2, 3])
        pygame.draw.circle(surface, (brightness, brightness, 200), (sx, sy), size)
    bright_stars = [(150, 100), (400, 80), (650, 120), (850, 90), (200, 200), (800, 180)]
    for bx, by in bright_stars:
        points = [
            (bx, by - 8),
            (bx - 2, by - 2),
            (bx - 8, by),
            (bx - 2, by + 2),
            (bx, by + 8),
            (bx + 2, by + 2),
            (bx + 8, by),
            (bx + 2, by - 2),
        ]
        pygame.draw.polygon(surface, (255, 255, 200), points)
        pygame.draw.circle(surface, (255, 255, 220), (bx, by), 3)
    pygame.draw.circle(surface, (240, 240, 255), (150, 150), 50)
    pygame.draw.circle(surface, (220, 220, 240), (150, 150), 45)
    pygame.draw.circle(surface, (200, 200, 220), (140, 140), 8)
    pygame.draw.circle(surface, (200, 200, 220), (160, 155), 6)
    pygame.draw.circle(surface, (200, 200, 220), (155, 165), 5)
    for i in range(10, 0, -1):
        alpha_color = (200, 200, 255)
        pygame.draw.circle(surface, alpha_color, (150, 150), 50 + i * 3, 2)
    mountain_points = [
        (0, 450), (150, 350), (300, 380), (450, 320), (600, 360), (750, 300), (900, 340), (1000, 380), (1000, 700), (0, 700)
    ]
    pygame.draw.polygon(surface, (10, 10, 30), mountain_points)
    pygame.draw.rect(surface, (20, 40, 20), (0, WINDOW_HEIGHT - 150, WINDOW_WIDTH, 150))
    for i in range(0, WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        pygame.draw.line(surface, (15, 35, 15),
                        (i, WINDOW_HEIGHT - 150),
                        (i, WINDOW_HEIGHT - 150 + grass_height), 2)
    glow_colors = [(150, 100, 200), (100, 150, 255), (200, 100, 200), (255, 150, 200)]
    for _ in range(20):
        fx = random.randint(50, WINDOW_WIDTH - 50)
        fy = random.randint(WINDOW_HEIGHT - 140, WINDOW_HEIGHT - 50)
        glow_color = random.choice(glow_colors)
        for i in range(3, 0, -1):
            glow_alpha = glow_color
            pygame.draw.circle(surface, glow_alpha, (fx, fy), 5 + i * 2)
        pygame.draw.circle(surface, glow_color, (fx, fy), 4)
    tree_positions = [(100, WINDOW_HEIGHT - 150), (300, WINDOW_HEIGHT - 150), 
                      (700, WINDOW_HEIGHT - 150), (900, WINDOW_HEIGHT - 150)]
    for tx, ty in tree_positions:
        pygame.draw.rect(surface, (20, 20, 20), (tx - 15, ty - 80, 30, 80))
        for i in range(5):
            offset_x = random.randint(-30, 30)
            offset_y = random.randint(-40, -20)
            pygame.draw.circle(surface, (10, 20, 10), (tx + offset_x, ty - 60 + offset_y), 25)
        pygame.draw.circle(surface, (15, 25, 15), (tx, ty - 70), 30)
        pygame.draw.circle(surface, (15, 25, 15), (tx - 15, ty - 60), 25)
        pygame.draw.circle(surface, (15, 25, 15), (tx + 15, ty - 60), 25)
    return surface
def create_dream_background():
    surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    for y in range(WINDOW_HEIGHT):
        ratio = y / WINDOW_HEIGHT
        r = int(216 * (1 - ratio) + 255 * ratio)
        g = int(191 * (1 - ratio) + 210 * ratio)
        b = int(216 * (1 - ratio) + 220 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WINDOW_WIDTH, y))
    for _ in range(150):
        sx = random.randint(0, WINDOW_WIDTH)
        sy = random.randint(0, WINDOW_HEIGHT)
        size = random.choice([1, 2, 3])
        brightness = random.randint(200, 255)
        color = random.choice([(brightness, brightness, 255), (255, brightness, brightness), (brightness, 255, brightness)])
        pygame.draw.circle(surface, color, (sx, sy), size)
    orb_colors = [(255, 200, 255), (200, 255, 255), (255, 255, 200), (255, 200, 200)]
    for _ in range(20):
        ox = random.randint(50, WINDOW_WIDTH - 50)
        oy = random.randint(50, WINDOW_HEIGHT - 50)
        orb_color = random.choice(orb_colors)
        orb_size = random.randint(15, 35)
        for i in range(5, 0, -1):
            alpha_val = 100 - i * 15
            pygame.draw.circle(surface, orb_color, (ox, oy), orb_size + i * 3)
        pygame.draw.circle(surface, orb_color, (ox, oy), orb_size)
    cloud_colors = [(255, 220, 255), (220, 255, 255), (255, 255, 220)]
    for _ in range(8):
        cx = random.randint(0, WINDOW_WIDTH)
        cy = random.randint(0, WINDOW_HEIGHT - 200)
        cloud_color = random.choice(cloud_colors)
        pygame.draw.ellipse(surface, cloud_color, (cx, cy, 150, 60))
        pygame.draw.ellipse(surface, cloud_color, (cx + 30, cy - 20, 100, 70))
        pygame.draw.ellipse(surface, cloud_color, (cx + 80, cy - 10, 90, 60))
    pygame.draw.rect(surface, (255, 220, 230), (0, WINDOW_HEIGHT - 150, WINDOW_WIDTH, 150))
    for i in range(0, WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        grass_color = random.choice([(200, 150, 200), (220, 180, 220), (240, 200, 240)])
        pygame.draw.line(surface, grass_color,
                        (i, WINDOW_HEIGHT - 150),
                        (i, WINDOW_HEIGHT - 150 + grass_height), 2)
    for _ in range(40):
        fx = random.randint(50, WINDOW_WIDTH - 50)
        fy = random.randint(WINDOW_HEIGHT - 140, WINDOW_HEIGHT - 50)
        flower_color = random.choice([(255, 150, 200), (200, 150, 255), (150, 200, 255), (255, 200, 150)])
        pygame.draw.line(surface, (150, 255, 150), (fx, fy), (fx, fy + 15), 3)
        for j in range(6):
            angle = j * (2 * math.pi / 6)
            petal_x = fx + math.cos(angle) * 6
            petal_y = fy + math.sin(angle) * 6
            pygame.draw.circle(surface, flower_color, (int(petal_x), int(petal_y)), 4)
        pygame.draw.circle(surface, (255, 255, 200), (fx, fy), 3)
    return surface
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
class Character:
    def __init__(self, x: float, y: float, scale: int = 4):
        self.x = x
        self.y = y
        self.scale = scale
        self.anim_frame = 0
        self.anim_timer = 0
        self.facing_right = True
        self.walking = False
    def update(self, dt: float):
        self.anim_timer += dt
        if self.anim_timer > 0.2:
            self.anim_timer = 0
            if self.walking:
                self.anim_frame = (self.anim_frame + 1) % 4
            else:
                self.anim_frame = (self.anim_frame + 1) % 8
class Beenie(Character):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, scale=5)
        self.sleeping = False
        self.sleep_timer = 0
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
            (x, y), (x+pixel, y), (x+2*pixel, y), (x+3*pixel, y), (x+4*pixel, y), (x+5*pixel, y),
            (x, y+pixel), (x+pixel, y+pixel), (x+4*pixel, y+pixel), (x+5*pixel, y+pixel),
            (x, y+2*pixel), (x+5*pixel, y+2*pixel),
        ]
        for pos in hair_positions:
            pygame.draw.rect(screen, BLACK, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(screen, ROSE_RED, (x+5*pixel, y+pixel, pixel, pixel))
        pygame.draw.rect(screen, ROSE_RED, (x+6*pixel, y+pixel, pixel//2, pixel))
        face_color = (255, 220, 200)
        face_positions = [
            (x+pixel, y+2*pixel), (x+2*pixel, y+2*pixel), (x+3*pixel, y+2*pixel), (x+4*pixel, y+2*pixel),
            (x+pixel, y+3*pixel), (x+2*pixel, y+3*pixel), (x+3*pixel, y+3*pixel), (x+4*pixel, y+3*pixel),
            (x+2*pixel, y+4*pixel), (x+3*pixel, y+4*pixel),
        ]
        for pos in face_positions:
            pygame.draw.rect(screen, face_color, (pos[0], pos[1] + breath_offset, pixel, pixel))
        blink = self.anim_frame == 7
        if not blink:
            pygame.draw.rect(screen, BLACK, (x+pixel+pixel//3, y+2*pixel+pixel//2 + breath_offset, pixel//2, pixel//2))
            pygame.draw.rect(screen, WHITE, (x+pixel+pixel//2, y+2*pixel+pixel//2 + breath_offset, pixel//4, pixel//4))
            pygame.draw.rect(screen, BLACK, (x+3*pixel+pixel//3, y+2*pixel+pixel//2 + breath_offset, pixel//2, pixel//2))
            pygame.draw.rect(screen, WHITE, (x+3*pixel+pixel//2, y+2*pixel+pixel//2 + breath_offset, pixel//4, pixel//4))
        else:
            pygame.draw.line(screen, BLACK, 
                           (x+pixel, y+2*pixel+pixel//2 + breath_offset),
                           (x+2*pixel-pixel//2, y+2*pixel+pixel//2 + breath_offset), 2)
            pygame.draw.line(screen, BLACK,
                           (x+3*pixel, y+2*pixel+pixel//2 + breath_offset),
                           (x+4*pixel-pixel//2, y+2*pixel+pixel//2 + breath_offset), 2)
        pygame.draw.rect(screen, SOFT_PINK, (x+pixel//2, y+3*pixel + breath_offset, pixel, pixel//2))
        pygame.draw.rect(screen, SOFT_PINK, (x+4*pixel+pixel//2, y+3*pixel + breath_offset, pixel, pixel//2))
        smile_points = [
            (x+2*pixel, y+3*pixel+pixel//2 + breath_offset),
            (x+2*pixel+pixel//2, y+3*pixel+pixel - pixel//4 + breath_offset),
            (x+3*pixel+pixel//2, y+3*pixel+pixel - pixel//4 + breath_offset),
            (x+4*pixel, y+3*pixel+pixel//2 + breath_offset),
        ]
        pygame.draw.lines(screen, DEEP_RED, False, smile_points, 2)
        pygame.draw.rect(screen, face_color, (x+2*pixel, y+5*pixel + breath_offset, pixel*2, pixel))
        dress_positions = [
            (x+pixel, y+5*pixel), (x+2*pixel, y+5*pixel), (x+3*pixel, y+5*pixel), (x+4*pixel, y+5*pixel),
            (x+pixel, y+6*pixel), (x+2*pixel, y+6*pixel), (x+3*pixel, y+6*pixel), (x+4*pixel, y+6*pixel),
            (x, y+7*pixel), (x+pixel, y+7*pixel), (x+2*pixel, y+7*pixel), 
            (x+3*pixel, y+7*pixel), (x+4*pixel, y+7*pixel), (x+5*pixel, y+7*pixel),
            (x, y+8*pixel), (x+pixel, y+8*pixel), (x+2*pixel, y+8*pixel),
            (x+3*pixel, y+8*pixel), (x+4*pixel, y+8*pixel), (x+5*pixel, y+8*pixel), (x+6*pixel, y+8*pixel),
            (x, y+9*pixel), (x+pixel, y+9*pixel), (x+2*pixel, y+9*pixel),
            (x+3*pixel, y+9*pixel), (x+4*pixel, y+9*pixel), (x+5*pixel, y+9*pixel), (x+6*pixel, y+9*pixel),
        ]
        for pos in dress_positions:
            pygame.draw.rect(screen, ROSE_RED, (pos[0], pos[1] + breath_offset, pixel, pixel))
        highlight_color = (255, 100, 120)
        pygame.draw.rect(screen, highlight_color, (x+2*pixel, y+6*pixel + breath_offset, pixel, pixel))
        if self.walking and self.anim_frame % 2 == 0:
            pygame.draw.rect(screen, face_color, (x+pixel, y+10*pixel + breath_offset, pixel, pixel*2))
            pygame.draw.rect(screen, face_color, (x+4*pixel, y+10*pixel+pixel + breath_offset, pixel, pixel))
        else:
            pygame.draw.rect(screen, face_color, (x+2*pixel, y+10*pixel + breath_offset, pixel, pixel*2))
            pygame.draw.rect(screen, face_color, (x+3*pixel, y+10*pixel + breath_offset, pixel, pixel*2))
    def draw_sleeping(self, screen: pygame.Surface, x: int, y: int, pixel: int):
        ground_y = y + (6 * pixel)
        pygame.draw.rect(screen, BLACK, (x, ground_y, 4*pixel, 4*pixel))
        face_color = (255, 220, 200)
        pygame.draw.rect(screen, face_color, (x + 1*pixel, ground_y + 1*pixel, 3*pixel, 3*pixel))
        pygame.draw.rect(screen, BLACK, (x + 2*pixel, ground_y + 2*pixel, pixel, 1))
        pygame.draw.rect(screen, ROSE_RED, (x + 4*pixel, ground_y + 1*pixel, 5*pixel, 3*pixel))
        pygame.draw.rect(screen, ROSE_RED, (x + 4*pixel, ground_y + 1*pixel, pixel, pixel))
        pygame.draw.rect(screen, face_color, (x + 9*pixel, ground_y + 2*pixel, 1*pixel, 2*pixel))
        current_time = pygame.time.get_ticks()
        if (current_time // 600) % 2 == 0:  
            font = pygame.font.Font(None, 24)
            z_surf = font.render("Z", True, WINE_RED)
            screen.blit(z_surf, (x + 2*pixel, ground_y - 20))
            if (current_time // 300) % 2 == 0:
                z_small = font.render("z", True, WINE_RED)
                screen.blit(z_small, (x + 4*pixel, ground_y - 35))
class Ahmad(Character):
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
            (x, y), (x+pixel, y), (x+2*pixel, y), (x+3*pixel, y), (x+4*pixel, y), (x+5*pixel, y),
            (x, y+pixel), (x+5*pixel, y+pixel),
            (x, y+2*pixel), (x+5*pixel, y+2*pixel),
        ]
        for pos in hair_positions:
            pygame.draw.rect(screen, BLACK, (pos[0], pos[1] + breath_offset, pixel, pixel))
        face_color = (255, 220, 190)
        face_positions = [
            (x+pixel, y+pixel), (x+2*pixel, y+pixel), (x+3*pixel, y+pixel), (x+4*pixel, y+pixel),
            (x+pixel, y+2*pixel), (x+2*pixel, y+2*pixel), (x+3*pixel, y+2*pixel), (x+4*pixel, y+2*pixel),
            (x+pixel, y+3*pixel), (x+2*pixel, y+3*pixel), (x+3*pixel, y+3*pixel), (x+4*pixel, y+3*pixel),
            (x+2*pixel, y+4*pixel), (x+3*pixel, y+4*pixel),
        ]
        for pos in face_positions:
            pygame.draw.rect(screen, face_color, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(screen, BLACK, (x+pixel+pixel//2, y+2*pixel+pixel//2 + breath_offset, pixel//2, pixel//2))
        pygame.draw.rect(screen, WHITE, (x+pixel+pixel//2+pixel//4, y+2*pixel+pixel//2 + breath_offset, pixel//4, pixel//4))
        pygame.draw.rect(screen, BLACK, (x+3*pixel+pixel//2, y+2*pixel+pixel//2 + breath_offset, pixel//2, pixel//2))
        pygame.draw.rect(screen, WHITE, (x+3*pixel+pixel//2+pixel//4, y+2*pixel+pixel//2 + breath_offset, pixel//4, pixel//4))
        smile_points = [
            (x+2*pixel, y+3*pixel+pixel//2 + breath_offset),
            (x+2*pixel+pixel//2, y+3*pixel+pixel + breath_offset),
            (x+3*pixel+pixel//2, y+3*pixel+pixel + breath_offset),
            (x+4*pixel, y+3*pixel+pixel//2 + breath_offset),
        ]
        pygame.draw.lines(screen, DEEP_RED, False, smile_points, 2)
        pygame.draw.rect(screen, face_color, (x+2*pixel, y+5*pixel + breath_offset, pixel*2, pixel))
        shirt_color = (40, 60, 100)
        shirt_positions = [
            (x+pixel, y+5*pixel), (x+2*pixel, y+5*pixel), (x+3*pixel, y+5*pixel), (x+4*pixel, y+5*pixel),
            (x+pixel, y+6*pixel), (x+2*pixel, y+6*pixel), (x+3*pixel, y+6*pixel), (x+4*pixel, y+6*pixel),
            (x+pixel, y+7*pixel), (x+2*pixel, y+7*pixel), (x+3*pixel, y+7*pixel), (x+4*pixel, y+7*pixel),
            (x+2*pixel, y+8*pixel), (x+3*pixel, y+8*pixel),
        ]
        for pos in shirt_positions:
            pygame.draw.rect(screen, shirt_color, (pos[0], pos[1] + breath_offset, pixel, pixel))
        pygame.draw.rect(screen, BLACK, (x+pixel, y+9*pixel + breath_offset, pixel*2, pixel*3))
        pygame.draw.rect(screen, BLACK, (x+3*pixel, y+9*pixel + breath_offset, pixel*2, pixel*3))
        pygame.draw.rect(screen, (60, 40, 20), (x+pixel, y+12*pixel + breath_offset, pixel*2, pixel))
        pygame.draw.rect(screen, (60, 40, 20), (x+3*pixel, y+12*pixel + breath_offset, pixel*2, pixel))
        if self.holding_rose:
            rose_x = x + 6*pixel if self.facing_right else x - 4*pixel
            rose_y = y + 6*pixel + breath_offset
            pygame.draw.rect(screen, (0, 120, 0), (rose_x+pixel//2, rose_y, pixel//2, pixel*3))
            pygame.draw.rect(screen, (0, 150, 0), (rose_x, rose_y+pixel, pixel, pixel//2))
            pygame.draw.rect(screen, (0, 150, 0), (rose_x+pixel, rose_y+pixel*2, pixel, pixel//2))
            petal_positions = [
                (rose_x, rose_y-pixel), (rose_x+pixel, rose_y-pixel),
                (rose_x-pixel//2, rose_y-pixel//2), (rose_x+pixel+pixel//2, rose_y-pixel//2),
                (rose_x+pixel//2, rose_y-pixel-pixel//2),
            ]
            for pos in petal_positions:
                pygame.draw.rect(screen, ROSE_RED, (pos[0], pos[1], pixel, pixel))
            pygame.draw.rect(screen, DEEP_RED, (rose_x+pixel//2, rose_y-pixel//2, pixel, pixel))
class Background:
    def __init__(self):
        self.time_of_day = "day"  
        self.day_bg = create_day_background()
        self.night_bg = create_night_background()
        self.dream_bg = create_dream_background()
        self.current_bg = self.day_bg
    def set_time(self, time: str):
        self.time_of_day = time
        if time == "day" or time == "evening":
            self.current_bg = self.day_bg
        elif time == "night":
            self.current_bg = self.night_bg
        elif time == "dream":
            self.current_bg = self.dream_bg
    def update(self, dt: float):
        pass
    def draw(self, screen: pygame.Surface):
        screen.blit(self.current_bg, (0, 0))
class DialogueBox:
    def __init__(self):
        self.active = False
        self.message = ""
        self.speaker = ""
        self.timer = 0
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
        box_x = (WINDOW_WIDTH - box_width) // 2
        box_y = WINDOW_HEIGHT - box_height - 20
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, ROSE_RED, (box_x, box_y, box_width, box_height), 4)
        font_name = pygame.font.Font(None, 32)
        name_text = font_name.render(self.speaker, True, WINE_RED)
        screen.blit(name_text, (box_x + 20, box_y + 10))
        font_msg = pygame.font.Font(None, 28)
        words = self.message.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font_msg.size(test_line)[0] < box_width - 40:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        y_offset = box_y + 45
        for line in lines[:2]:  
            msg_text = font_msg.render(line, True, BLACK)
            screen.blit(msg_text, (box_x + 20, y_offset))
            y_offset += 30
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Beenie kay liyeee Gameeee")
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        try:
            pygame.mixer.music.load("music.mp3") 
            pygame.mixer.music.set_volume(0.5)  
            pygame.mixer.music.play(-1)         
        except pygame.error as e:
            print(f"Could not load music file: {e}")
        self.state = STATE_TITLE
        self.state_timer = 0
        self.beenie = Beenie(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 200)
        self.ahmad = Ahmad(-200, WINDOW_HEIGHT - 200)
        self.background = Background()
        self.particles: List[Particle] = []
        self.thoughts: List[dict] = []
        self.thought_timer = 0
        self.dialogue = DialogueBox()
        self.fade_alpha = 0
        self.fading_in = False
        self.fading_out = False
        self.message = ""
        self.message_timer = 0
        self.title_pulse = 0
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == STATE_TITLE:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.state = STATE_INTRO
                        self.state_timer = 0
    def update(self, dt: float):
        self.state_timer += dt
        self.background.update(dt)
        self.beenie.update(dt)
        self.ahmad.update(dt)
        if self.beenie.sleeping:
            self.beenie.sleep_timer += dt
        self.dialogue.update(dt)
        if self.state == STATE_TITLE:
            self.update_title(dt)
        elif self.state == STATE_INTRO:
            self.update_intro(dt)
        elif self.state == STATE_WANDER:
            self.update_wander(dt)
        elif self.state == STATE_MEETING:
            self.update_meeting(dt)
        elif self.state == STATE_CONVERSATION:
            self.update_conversation(dt)
        elif self.state == STATE_SLEEP_TRANSITION:
            self.update_sleep_transition(dt)
        elif self.state == STATE_SLEEP:
            self.update_sleep(dt)
        elif self.state == STATE_DREAM:
            self.update_dream(dt)
        elif self.state == STATE_WAKE_TRANSITION:
            self.update_wake_transition(dt)
        elif self.state == STATE_REVEAL:
            self.update_reveal(dt)
        elif self.state == STATE_KISS:
            self.update_kiss(dt)
        elif self.state == STATE_MARRIAGE:
            self.update_marriage(dt)
        elif self.state == STATE_END:
            self.update_end(dt)
        self.update_particles(dt)
        self.update_fade(dt)
    def update_title(self, dt: float):
        self.title_pulse += dt
        self.background.set_time("day")
        if random.random() < 0.1:
            self.spawn_rose_petal()
        if random.random() < 0.05:
            self.spawn_heart(random.randint(100, WINDOW_WIDTH - 100), -20)
    def update_intro(self, dt: float):
        self.background.set_time("day")
        if random.random() < 0.2:
            self.spawn_snow()
        keys = pygame.key.get_pressed()
        speed = 80 * dt
        moved = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.beenie.x -= speed
            self.beenie.facing_right = False
            moved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.beenie.x += speed
            self.beenie.facing_right = True
            moved = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.beenie.y -= speed
            moved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.beenie.y += speed
            moved = True
        self.beenie.walking = moved
        self.beenie.x = max(50, min(WINDOW_WIDTH - 150, self.beenie.x))
        self.beenie.y = max(WINDOW_HEIGHT - 210, min(WINDOW_HEIGHT - 100, self.beenie.y))
        if self.state_timer < 4:
            self.message = "Kal ka din...."
        else:
            self.message = ""
        if self.state_timer > 8:
            self.state = STATE_WANDER
            self.state_timer = 0
    def update_wander(self, dt: float):
        keys = pygame.key.get_pressed()
        speed = 80 * dt
        moved = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.beenie.x -= speed
            self.beenie.facing_right = False
            moved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.beenie.x += speed
            self.beenie.facing_right = True
            moved = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.beenie.y -= speed
            moved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.beenie.y += speed
            moved = True
        self.beenie.walking = moved
        self.beenie.x = max(50, min(WINDOW_WIDTH - 150, self.beenie.x))
        self.beenie.y = max(WINDOW_HEIGHT - 250, min(WINDOW_HEIGHT - 100, self.beenie.y))
        if random.random() < 0.15:
            self.spawn_snow()
        if random.random() < 0.1:
            self.spawn_sparkle(self.beenie.x + random.randint(-30, 30),
                             self.beenie.y + random.randint(-30, 30))
        self.thought_timer += dt
        if self.thought_timer > 4.0:
            self.thought_timer = 0
            self.spawn_thought()
        for thought in self.thoughts[:]:
            thought['y'] -= 15 * dt
            thought['life'] -= dt
            thought['x'] += math.sin(thought['life'] * 2) * 0.5
            if thought['life'] <= 0:
                self.thoughts.remove(thought)
        if self.state_timer > 15:
            self.state = STATE_MEETING
            self.state_timer = 0
            self.dialogue.show("", "waohhh.....koi a rha hayyyy....", 3.0)
    def update_meeting(self, dt: float):
        if self.ahmad.x < self.beenie.x - 120:
            self.ahmad.x += 60 * dt
            self.ahmad.facing_right = True
            self.ahmad.walking = True
        else:
            self.ahmad.walking = False
        if random.random() < 0.1:
            self.spawn_snow()
        if self.state_timer > 6:
            self.state = STATE_CONVERSATION
            self.state_timer = 0
            self.dialogue.show("Ahmad", "Kesi hain meri pyari jaaannnn...", 4.0)
    def update_conversation(self, dt: float):
        if random.random() < 0.08:
            self.spawn_snow()
        if self.state_timer > 4 and self.state_timer < 4.1:
            self.dialogue.show("Beenie", "Theak hun.....", 4.0)
        elif self.state_timer > 9 and self.state_timer < 9.1:
            self.dialogue.show("Ahmad", "Aryyy, sirif theak, ap to itii thaki thaki lag rahi hain, thoru sa so jayen naww...", 4.0)
        elif self.state_timer > 14 and self.state_timer < 14.1:
            self.dialogue.show("Beenie", "ohhh....okieeee...", 3.0)
        if self.state_timer > 18:
            self.state = STATE_SLEEP_TRANSITION
            self.state_timer = 0
    def update_sleep_transition(self, dt: float):
        if self.state_timer > 2:
            self.beenie.sleeping = True
        if random.random() < 0.15:
            self.spawn_dream_particle()
        if self.state_timer > 4 and self.state_timer < 4.1:
            self.start_fade_out()
        if self.state_timer > 6:
            self.state = STATE_SLEEP
            self.state_timer = 0
            self.background.set_time("evening")
    def update_sleep(self, dt: float):
        if self.ahmad.x > -200:
            self.ahmad.x -= 50 * dt
            self.ahmad.facing_right = False
            self.ahmad.walking = True
        if random.random() < 0.2:
            self.spawn_dream_particle()
        if self.state_timer > 8:
            self.state = STATE_DREAM
            self.state_timer = 0
            self.background.set_time("dream")
            self.ahmad.holding_rose = True
            self.ahmad.x = -200
            self.start_fade_in()
    def update_dream(self, dt: float):
        if random.random() < 0.3:
            self.spawn_dream_particle()
        if random.random() < 0.1:
            self.spawn_sparkle(random.randint(0, WINDOW_WIDTH),
                             random.randint(0, WINDOW_HEIGHT))
        if random.random() < 0.15:
            self.spawn_rose_petal()
        if self.state_timer > 10:
            self.state = STATE_WAKE_TRANSITION
            self.state_timer = 0
            self.background.set_time("evening")
    def update_wake_transition(self, dt: float):
        if self.ahmad.x < self.beenie.x - 100:
            self.ahmad.x += 70 * dt
            self.ahmad.facing_right = True
            self.ahmad.walking = True
        else:
            self.ahmad.walking = False
        if random.random() < 0.1:
            self.spawn_rose_petal()
        if self.state_timer > 5:
            self.state = STATE_REVEAL
            self.state_timer = 0
            self.dialogue.show("Ahmad", "Yae Phul, meri Rosey kay liye, Meri Ghulabo kay liye... I love you, meri pyari jaan. Happy Rose Day! 🌹", 5.0)
    def update_reveal(self, dt: float):
        if random.random() < 0.2:
            self.spawn_rose_petal()
        if random.random() < 0.15:
            self.spawn_sparkle(self.ahmad.x + random.randint(-40, 40),
                             self.ahmad.y + random.randint(-40, 40))
        if self.state_timer > 3:
            self.beenie.sleeping = False
        if self.state_timer > 8:
            self.state = STATE_KISS
            self.state_timer = 0
    def update_kiss(self, dt: float):
        if abs(self.ahmad.x - self.beenie.x) > 60:
            self.ahmad.x += 30 * dt
        if self.state_timer > 2 and self.state_timer < 2.5:
            for _ in range(20):
                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(50, 150)
                self.particles.append(Particle(
                    x=self.beenie.x + 20,
                    y=self.beenie.y - 20,
                    vx=math.cos(angle) * speed,
                    vy=math.sin(angle) * speed - 50,
                    life=random.uniform(1.5, 3.0),
                    max_life=3.0,
                    color=HEART_RED,
                    size=8,
                    particle_type="heart"
                ))
        if random.random() < 0.3:
            self.spawn_heart(self.beenie.x + random.randint(-50, 50),
                           self.beenie.y - random.randint(20, 60))
        if random.random() < 0.2:
            self.spawn_rose_petal()
        if self.state_timer > 7:
            self.state = STATE_MARRIAGE
            self.state_timer = 0
            self.background.set_time("night")
    def update_marriage(self, dt: float):
        if random.random() < 0.5:
            self.spawn_rose_petal()
        if random.random() < 0.4:
            self.spawn_heart(random.randint(100, WINDOW_WIDTH - 100),
                           random.randint(-20, WINDOW_HEIGHT // 2))
        if random.random() < 0.3:
            self.spawn_sparkle(random.randint(0, WINDOW_WIDTH),
                             random.randint(0, WINDOW_HEIGHT))
        if self.state_timer < 5:
            self.message = "Happy Rose Day, Beenie Beghum"
        elif self.state_timer < 10:
            self.message = "Thenkeww for being my roseyy, or red red apki cheeks and nosey. Allah talla meri pyar beghum ki cheeks ko asy hi hasta muskurata and rose red rakhy"
        else:
            self.message = ""
        if self.state_timer > 12:
            self.state = STATE_END
            self.state_timer = 0
    def update_end(self, dt: float):
        if random.random() < 0.4:
            self.spawn_rose_petal()
        if random.random() < 0.3:
            self.spawn_heart(random.randint(100, WINDOW_WIDTH - 100),
                           random.randint(-20, WINDOW_HEIGHT // 2))
        if random.random() < 0.2:
            self.spawn_sparkle(random.randint(0, WINDOW_WIDTH),
                             random.randint(0, WINDOW_HEIGHT))
        self.message = "Me rasgulla, my roseie, meri golgappa, My Shamooo...MUUAAHHH. \nHappy Rose Day Meri Pyari Beghum "
    def update_particles(self, dt: float):
        for particle in self.particles[:]:
            if particle.particle_type in ["rose_petal", "heart"]:
                particle.vy += 50 * dt  
            particle.x += particle.vx * dt
            particle.y += particle.vy * dt
            particle.life -= dt
            if particle.life <= 0:
                self.particles.remove(particle)
    def update_fade(self, dt: float):
        if self.fading_out:
            self.fade_alpha += 150 * dt
            if self.fade_alpha >= 255:
                self.fade_alpha = 255
                self.fading_out = False
        if self.fading_in:
            self.fade_alpha -= 150 * dt
            if self.fade_alpha <= 0:
                self.fade_alpha = 0
                self.fading_in = False
    def spawn_snow(self):
        self.particles.append(Particle(
            x=random.randint(0, WINDOW_WIDTH),
            y=-10,
            vx=random.uniform(-15, 15),
            vy=random.uniform(30, 70),
            life=random.uniform(10, 15),
            max_life=15,
            color=WHITE,
            size=random.randint(2, 5),
            particle_type="snow"
        ))
    def spawn_rose_petal(self):
        self.particles.append(Particle(
            x=random.randint(0, WINDOW_WIDTH),
            y=-10,
            vx=random.uniform(-25, 25),
            vy=random.uniform(10, 30),
            life=random.uniform(8, 12),
            max_life=12,
            color=random.choice([ROSE_RED, SOFT_PINK, DEEP_RED]),
            size=random.randint(4, 8),
            particle_type="rose_petal"
        ))
    def spawn_heart(self, x: float, y: float):
        self.particles.append(Particle(
            x=x + random.uniform(-20, 20),
            y=y,
            vx=random.uniform(-20, 20),
            vy=random.uniform(-100, -40),
            life=random.uniform(2.5, 4.5),
            max_life=4.5,
            color=HEART_RED,
            size=random.randint(6, 10),
            particle_type="heart"
        ))
    def spawn_dream_particle(self):
        self.particles.append(Particle(
            x=random.randint(0, WINDOW_WIDTH),
            y=random.randint(0, WINDOW_HEIGHT),
            vx=random.uniform(-15, 15),
            vy=random.uniform(-15, 15),
            life=random.uniform(4, 8),
            max_life=8,
            color=random.choice([DREAMY_PINK, LIGHT_PURPLE, SOFT_PINK]),
            size=random.randint(4, 10),
            particle_type="dream"
        ))
    def spawn_sparkle(self, x: float, y: float):
        self.particles.append(Particle(
            x=x,
            y=y,
            vx=random.uniform(-10, 10),
            vy=random.uniform(-10, 10),
            life=random.uniform(0.5, 1.5),
            max_life=1.5,
            color=STAR_YELLOW,
            size=random.randint(2, 4),
            particle_type="sparkle"
        ))
    def spawn_thought(self):
        thought_type = random.choice(['wolf', 'rose', 'noodles'])
        self.thoughts.append({
            'type': thought_type,
            'x': self.beenie.x + 30,
            'y': self.beenie.y - 60,
            'life': 5.0
        })
    def start_fade_out(self):
        self.fading_out = True
        self.fade_alpha = 0
    def start_fade_in(self):
        self.fading_in = True
        self.fade_alpha = 255
    def draw(self):
        self.background.draw(self.screen)
        for particle in self.particles:
            if particle.particle_type in ["snow", "rose_petal"]:
                self.draw_particle(particle)
        if self.ahmad.x > -100:
            self.ahmad.draw(self.screen)
        self.beenie.draw(self.screen)
        for particle in self.particles:
            if particle.particle_type not in ["snow", "rose_petal"]:
                self.draw_particle(particle)
        for thought in self.thoughts:
            self.draw_thought(thought)
        self.dialogue.draw(self.screen)
        if self.message:
            self.draw_message()
        if self.state == STATE_TITLE:
            self.draw_title_screen()
        if self.fade_alpha > 0:
            fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(int(self.fade_alpha))
            self.screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
    def draw_particle(self, particle: Particle):
        alpha_ratio = particle.life / particle.max_life
        if particle.particle_type == "heart":
            self.draw_heart(particle.x, particle.y, particle.size, particle.color, alpha_ratio)
        elif particle.particle_type == "sparkle":
            size = int(particle.size * alpha_ratio)
            self.draw_star(particle.x, particle.y, size, particle.color)
        elif particle.particle_type == "rose_petal":
            size = particle.size
            angle = particle.life * 2
            for i in range(3):
                offset_x = math.cos(angle + i * 2) * size
                offset_y = math.sin(angle + i * 2) * size
                pygame.draw.circle(self.screen, particle.color,
                                 (int(particle.x + offset_x), int(particle.y + offset_y)),
                                 size // 2)
        else:
            size = int(particle.size * alpha_ratio) if alpha_ratio < 1 else particle.size
            pygame.draw.circle(self.screen, particle.color,
                             (int(particle.x), int(particle.y)), max(1, size))
    def draw_heart(self, x: float, y: float, size: int, color: Tuple[int, int, int], alpha: float = 1.0):
        s = max(1, int(size // 2 * alpha))
        positions = [
            (x-s, y), (x+s, y),
            (x-2*s, y+s), (x-s, y+s), (x, y+s), (x+s, y+s), (x+2*s, y+s),
            (x-2*s, y+2*s), (x-s, y+2*s), (x, y+2*s), (x+s, y+2*s), (x+2*s, y+2*s),
            (x-s, y+3*s), (x, y+3*s), (x+s, y+3*s),
            (x, y+4*s),
        ]
        for px, py in positions:
            pygame.draw.rect(self.screen, color, (int(px), int(py), s, s))
    def draw_star(self, x: float, y: float, size: int, color: Tuple[int, int, int]):
        points = [
            (x, y - size),
            (x - size//3, y - size//3),
            (x - size, y),
            (x - size//3, y + size//3),
            (x, y + size),
            (x + size//3, y + size//3),
            (x + size, y),
            (x + size//3, y - size//3),
        ]
        pygame.draw.polygon(self.screen, color, points)
    def draw_thought(self, thought: dict):
        x, y = int(thought['x']), int(thought['y'])
        pixel = 4
        alpha = min(1.0, thought['life'] / 2.0)
        bubble_radius = 25
        pygame.draw.circle(self.screen, WHITE, (x, y), bubble_radius)
        pygame.draw.circle(self.screen, ROSE_RED, (x, y), bubble_radius, 2)
        pygame.draw.circle(self.screen, WHITE, (x - 15, y + 20), 8)
        pygame.draw.circle(self.screen, ROSE_RED, (x - 15, y + 20), 8, 1)
        pygame.draw.circle(self.screen, WHITE, (x - 25, y + 30), 5)
        pygame.draw.circle(self.screen, ROSE_RED, (x - 25, y + 30), 5, 1)
        if thought['type'] == 'wolf':
            wolf_points = [
                (x - 10, y + 5), (x - 8, y - 5), (x - 5, y - 8),
                (x, y - 10), (x + 5, y - 8), (x + 8, y - 5),
                (x + 10, y + 5), (x + 5, y + 8), (x - 5, y + 8)
            ]
            pygame.draw.polygon(self.screen, (80, 80, 80), wolf_points)
            pygame.draw.circle(self.screen, STAR_YELLOW, (x - 3, y - 2), 2)
            pygame.draw.circle(self.screen, STAR_YELLOW, (x + 3, y - 2), 2)
        elif thought['type'] == 'rose':
            pygame.draw.rect(self.screen, (0, 120, 0), (x - 1, y + 2, 2, 12))
            leaf_points_left = [(x - 5, y + 6), (x - 1, y + 7), (x - 1, y + 10)]
            leaf_points_right = [(x + 5, y + 9), (x + 1, y + 10), (x + 1, y + 13)]
            pygame.draw.polygon(self.screen, (0, 150, 0), leaf_points_left)
            pygame.draw.polygon(self.screen, (0, 150, 0), leaf_points_right)
            for i in range(5):
                angle = i * (2 * math.pi / 5)
                petal_x = x + math.cos(angle) * 6
                petal_y = y - 5 + math.sin(angle) * 6
                pygame.draw.circle(self.screen, ROSE_RED, (int(petal_x), int(petal_y)), 4)
            pygame.draw.circle(self.screen, DEEP_RED, (x, y - 5), 3)
        elif thought['type'] == 'noodles':
            bowl_rect = pygame.Rect(x - 10, y + 2, 20, 12)
            pygame.draw.ellipse(self.screen, (200, 150, 100), bowl_rect)
            pygame.draw.ellipse(self.screen, (180, 130, 80), bowl_rect, 2)
            for i in range(4):
                start_x = x - 8 + i * 4
                points = [
                    (start_x, y - 5),
                    (start_x + 1, y - 3),
                    (start_x, y - 1),
                    (start_x + 1, y + 1)
                ]
                pygame.draw.lines(self.screen, (255, 220, 150), False, points, 2)
            pygame.draw.line(self.screen, (100, 60, 30), (x + 5, y - 8), (x + 12, y - 12), 2)
            pygame.draw.line(self.screen, (100, 60, 30), (x + 7, y - 8), (x + 14, y - 12), 2)
    def draw_message(self):
        if self.state == STATE_END:
            font_size = 40
        else:
            font_size = 36
        font = pygame.font.Font(None, font_size)
        words = self.message.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] < WINDOW_WIDTH - 100:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            lines.append(current_line.strip())
        y_offset = 80
        for i, line in enumerate(lines):
            text = font.render(line, True, WINE_RED)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y_offset + i * 50))
            bg_rect = text_rect.inflate(30, 15)
            for offset in range(5, 0, -1):
                glow_rect = bg_rect.inflate(offset * 2, offset * 2)
                glow_color = (255, 200, 200, 50 - offset * 10)
                pygame.draw.rect(self.screen, glow_color[:3], glow_rect, border_radius=10)
            pygame.draw.rect(self.screen, WHITE, bg_rect, border_radius=10)
            pygame.draw.rect(self.screen, ROSE_RED, bg_rect, 4, border_radius=10)
            self.screen.blit(text, text_rect)
    def draw_title_screen(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(100)
        self.screen.blit(overlay, (0, 0))
        title_font = pygame.font.Font(None, 80)
        pulse = abs(math.sin(self.title_pulse * 2))
        title_color = (
            int(ROSE_RED[0] * (0.7 + 0.3 * pulse)),
            int(ROSE_RED[1] * (0.7 + 0.3 * pulse)),
            int(ROSE_RED[2] * (0.7 + 0.3 * pulse))
        )
        title_text = title_font.render("Mazyyy wali Gameee", True, title_color)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        bg_rect = title_rect.inflate(40, 20)
        pygame.draw.rect(self.screen, WHITE, bg_rect, border_radius=15)
        pygame.draw.rect(self.screen, ROSE_RED, bg_rect, 5, border_radius=15)
        self.screen.blit(title_text, title_rect)
        subtitle_font = pygame.font.Font(None, 36)
        subtitle_text = subtitle_font.render("mazyy wali story", True, WINE_RED)
        subtitle_rect = subtitle_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
        self.screen.blit(subtitle_text, subtitle_rect)
        prompt_font = pygame.font.Font(None, 32)
        blink = int(self.title_pulse * 2) % 2 == 0
        if blink:
            prompt_text = prompt_font.render("Press SPACE or ENTER to begin", True, SOFT_PINK)
            prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
            self.screen.blit(prompt_text, prompt_rect)
        for i in range(3):
            offset_x = (i - 1) * 100
            self.draw_heart(WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 2 + 180, 8, HEART_RED)
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
if __name__ == "__main__":
    game = Game()
    game.run()