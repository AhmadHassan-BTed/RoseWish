import pygame
import math
import random
from src.config.settings import settings

def create_day_background():
    surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    for y in range(settings.WINDOW_HEIGHT):
        ratio = y / settings.WINDOW_HEIGHT
        r = int(135 * (1 - ratio) + 200 * ratio)
        g = int(206 * (1 - ratio) + 230 * ratio)
        b = int(250 * (1 - ratio) + 255 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (settings.WINDOW_WIDTH, y))
    
    # Sun
    pygame.draw.circle(surface, (255, 255, 200), (850, 120), 60)
    pygame.draw.circle(surface, (255, 255, 150), (850, 120), 50)
    for i in range(12):
        angle = i * (math.pi * 2 / 12)
        start_x = 850 + math.cos(angle) * 70
        start_y = 120 + math.sin(angle) * 70
        end_x = 850 + math.cos(angle) * 100
        end_y = 120 + math.sin(angle) * 100
        pygame.draw.line(surface, (255, 255, 180), (start_x, start_y), (end_x, end_y), 3)

    # Clouds
    cloud_positions = [(200, 100), (500, 150), (750, 80), (300, 200)]
    for cx, cy in cloud_positions:
        pygame.draw.ellipse(surface, (255, 255, 255), (cx, cy, 120, 40))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 20, cy - 15, 80, 50))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 60, cy - 10, 70, 45))
        pygame.draw.ellipse(surface, (255, 255, 255), (cx + 80, cy, 90, 35))

    # Mountains
    mountain_points = [
        (0, 400), (150, 300), (300, 350), (450, 280), (600, 320), (750, 260), (900, 300), (1000, 350), (1000, 700), (0, 700)
    ]
    pygame.draw.polygon(surface, (150, 180, 150), mountain_points)
    shadow_points = [(150, 300), (300, 350), (300, 700), (150, 700)]
    pygame.draw.polygon(surface, (130, 160, 130), shadow_points)
    shadow_points2 = [(600, 320), (750, 260), (750, 700), (600, 700)]
    pygame.draw.polygon(surface, (130, 160, 130), shadow_points2)

    # Grass
    pygame.draw.rect(surface, (144, 238, 144), (0, settings.WINDOW_HEIGHT - 150, settings.WINDOW_WIDTH, 150))
    for i in range(0, settings.WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        grass_shade = random.randint(100, 180)
        pygame.draw.line(surface, (grass_shade, 200, grass_shade),
                        (i, settings.WINDOW_HEIGHT - 150),
                        (i, settings.WINDOW_HEIGHT - 150 + grass_height), 2)

    # Flowers
    flower_colors = [(255, 100, 150), (255, 150, 200), (255, 200, 100), (200, 150, 255)]
    for _ in range(30):
        fx = random.randint(50, settings.WINDOW_WIDTH - 50)
        fy = random.randint(settings.WINDOW_HEIGHT - 140, settings.WINDOW_HEIGHT - 50)
        flower_color = random.choice(flower_colors)
        pygame.draw.line(surface, (0, 150, 0), (fx, fy), (fx, fy + 15), 2)
        for j in range(5):
            angle = j * (2 * math.pi / 5)
            petal_x = fx + math.cos(angle) * 5
            petal_y = fy + math.sin(angle) * 5
            pygame.draw.circle(surface, flower_color, (int(petal_x), int(petal_y)), 3)
        pygame.draw.circle(surface, (255, 200, 0), (fx, fy), 2)

    # Trees
    tree_positions = [(100, settings.WINDOW_HEIGHT - 150), (300, settings.WINDOW_HEIGHT - 150), 
                      (700, settings.WINDOW_HEIGHT - 150), (900, settings.WINDOW_HEIGHT - 150)]
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
    surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    for y in range(settings.WINDOW_HEIGHT):
        ratio = y / settings.WINDOW_HEIGHT
        r = int(15 * (1 - ratio) + 30 * ratio)
        g = int(15 * (1 - ratio) + 25 * ratio)
        b = int(40 * (1 - ratio) + 60 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (settings.WINDOW_WIDTH, y))
    
    for _ in range(200):
        sx = random.randint(0, settings.WINDOW_WIDTH)
        sy = random.randint(0, settings.WINDOW_HEIGHT // 2)
        brightness = random.randint(150, 255)
        size = random.choice([1, 1, 1, 2, 2, 3])
        pygame.draw.circle(surface, (brightness, brightness, 200), (sx, sy), size)

    bright_stars = [(150, 100), (400, 80), (650, 120), (850, 90), (200, 200), (800, 180)]
    for bx, by in bright_stars:
        points = [(bx, by-8), (bx-2, by-2), (bx-8, by), (bx-2, by+2), (bx, by+8), (bx+2, by+2), (bx+8, by), (bx+2, by-2)]
        pygame.draw.polygon(surface, (255, 255, 200), points)
        pygame.draw.circle(surface, (255, 255, 220), (bx, by), 3)

    # Moon
    pygame.draw.circle(surface, (240, 240, 255), (150, 150), 50)
    pygame.draw.circle(surface, (220, 220, 240), (150, 150), 45)
    pygame.draw.circle(surface, (200, 200, 220), (140, 140), 8)
    pygame.draw.circle(surface, (200, 200, 220), (160, 155), 6)
    pygame.draw.circle(surface, (200, 200, 220), (155, 165), 5)
    for i in range(10, 0, -1):
        pygame.draw.circle(surface, (200, 200, 255), (150, 150), 50 + i * 3, 2)

    mountain_points = [(0, 450), (150, 350), (300, 380), (450, 320), (600, 360), (750, 300), (900, 340), (1000, 380), (1000, 700), (0, 700)]
    pygame.draw.polygon(surface, (10, 10, 30), mountain_points)
    pygame.draw.rect(surface, (20, 40, 20), (0, settings.WINDOW_HEIGHT - 150, settings.WINDOW_WIDTH, 150))
    for i in range(0, settings.WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        pygame.draw.line(surface, (15, 35, 15), (i, settings.WINDOW_HEIGHT - 150), (i, settings.WINDOW_HEIGHT - 150 + grass_height), 2)
    
    glow_colors = [(150, 100, 200), (100, 150, 255), (200, 100, 200), (255, 150, 200)]
    for _ in range(20):
        fx = random.randint(50, settings.WINDOW_WIDTH - 50)
        fy = random.randint(settings.WINDOW_HEIGHT - 140, settings.WINDOW_HEIGHT - 50)
        glow_color = random.choice(glow_colors)
        for i in range(3, 0, -1):
            pygame.draw.circle(surface, glow_color, (fx, fy), 5 + i * 2)
        pygame.draw.circle(surface, glow_color, (fx, fy), 4)

    tree_positions = [(100, settings.WINDOW_HEIGHT - 150), (300, settings.WINDOW_HEIGHT - 150), 
                      (700, settings.WINDOW_HEIGHT - 150), (900, settings.WINDOW_HEIGHT - 150)]
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
    surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    for y in range(settings.WINDOW_HEIGHT):
        ratio = y / settings.WINDOW_HEIGHT
        r = int(216 * (1 - ratio) + 255 * ratio)
        g = int(191 * (1 - ratio) + 210 * ratio)
        b = int(216 * (1 - ratio) + 220 * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (settings.WINDOW_WIDTH, y))
    
    for _ in range(150):
        sx = random.randint(0, settings.WINDOW_WIDTH)
        sy = random.randint(0, settings.WINDOW_HEIGHT)
        size = random.choice([1, 2, 3])
        brightness = random.randint(200, 255)
        color = random.choice([(brightness, brightness, 255), (255, brightness, brightness), (brightness, 255, brightness)])
        pygame.draw.circle(surface, color, (sx, sy), size)

    # Orbs
    orb_colors = [(255, 200, 255), (200, 255, 255), (255, 255, 200), (255, 200, 200)]
    for _ in range(20):
        ox = random.randint(50, settings.WINDOW_WIDTH - 50)
        oy = random.randint(50, settings.WINDOW_HEIGHT - 50)
        orb_color = random.choice(orb_colors)
        orb_size = random.randint(15, 35)
        for i in range(5, 0, -1):
            pygame.draw.circle(surface, orb_color, (ox, oy), orb_size + i * 3)
        pygame.draw.circle(surface, orb_color, (ox, oy), orb_size)

    # Dream Clouds
    cloud_colors = [(255, 220, 255), (220, 255, 255), (255, 255, 220)]
    for _ in range(8):
        cx = random.randint(0, settings.WINDOW_WIDTH)
        cy = random.randint(0, settings.WINDOW_HEIGHT - 200)
        cloud_color = random.choice(cloud_colors)
        pygame.draw.ellipse(surface, cloud_color, (cx, cy, 150, 60))
        pygame.draw.ellipse(surface, cloud_color, (cx + 30, cy - 20, 100, 70))
        pygame.draw.ellipse(surface, cloud_color, (cx + 80, cy - 10, 90, 60))

    pygame.draw.rect(surface, (255, 220, 230), (0, settings.WINDOW_HEIGHT - 150, settings.WINDOW_WIDTH, 150))
    for i in range(0, settings.WINDOW_WIDTH, 5):
        grass_height = random.randint(5, 15)
        grass_color = random.choice([(200, 150, 200), (220, 180, 220), (240, 200, 240)])
        pygame.draw.line(surface, grass_color, (i, settings.WINDOW_HEIGHT - 150), (i, settings.WINDOW_HEIGHT - 150 + grass_height), 2)
    
    for _ in range(40):
        fx = random.randint(50, settings.WINDOW_WIDTH - 50)
        fy = random.randint(settings.WINDOW_HEIGHT - 140, settings.WINDOW_HEIGHT - 50)
        flower_color = random.choice([(255, 150, 200), (200, 150, 255), (150, 200, 255), (255, 200, 150)])
        pygame.draw.line(surface, (150, 255, 150), (fx, fy), (fx, fy + 15), 3)
        for j in range(6):
            angle = j * (2 * math.pi / 6)
            petal_x = fx + math.cos(angle) * 6
            petal_y = fy + math.sin(angle) * 6
            pygame.draw.circle(surface, flower_color, (int(petal_x), int(petal_y)), 4)
        pygame.draw.circle(surface, (255, 255, 200), (fx, fy), 3)
    return surface

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
