import pygame
import random
import math
from src.config.settings import settings
from src.core.registry import Registry
from src.core.event_bus import event_bus
from src.services.audio_service import AudioService
from src.services.render_service import RenderService
from src.utils.constants import GameState
from src.entities.miss_lovely import MissLovely
from src.entities.mr_lover import MrLover
from src.ui.background import Background
from src.ui.dialogue_box import DialogueBox
from src.utils.particles import ParticleManager, Particle
from src.utils.thoughts import ThoughtManager

class GameEngine:
    def __init__(self):
        self.renderer = RenderService()
        self.audio = AudioService()
        Registry.register(RenderService, self.renderer)
        Registry.register(AudioService, self.audio)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.TITLE
        self.state_timer = 0.0
        
        self.audio.play_music(settings.MUSIC_PATH)
        self.background = Background()
        self.particles = ParticleManager()
        self.thoughts = ThoughtManager()
        self.dialogue = DialogueBox()
        
        self.partner = MissLovely(settings.WINDOW_WIDTH // 2 - 100, settings.WINDOW_HEIGHT - 200)
        self.player = MrLover(-200, settings.WINDOW_HEIGHT - 200)
        
        self.message = ""
        self.title_pulse = 0.0
        self.fade_alpha = 0.0
        self.fading_in = False
        self.fading_out = False

        self.font_msg = pygame.font.Font(None, 36)
        self.font_end = pygame.font.Font(None, 40)
        self.font_title = pygame.font.Font(None, 80)
        self.font_subtitle = pygame.font.Font(None, 36)
        self.font_prompt = pygame.font.Font(None, 32)

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000.0
            self.handle_input()
            self.update(dt)
            self.render()
        pygame.quit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == GameState.TITLE:
                    if event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                        self.state = GameState.INTRO
                        self.state_timer = 0

    def update(self, dt: float):
        self.state_timer += dt
        self.background.update(dt)
        self.partner.update(dt)
        self.player.update(dt)
        if self.partner.sleeping:
            self.partner.sleep_timer += dt
        self.particles.update(dt)
        self.thoughts.update(dt)
        self.dialogue.update(dt)
        self.update_fade(dt)
        
        
        if self.state == GameState.TITLE:
            self.title_pulse += dt
            self.background.set_time("day")
            if random.random() < 0.1: self.particles.spawn_rose_petal()
            if random.random() < 0.05: self.particles.spawn_heart(random.randint(100, settings.WINDOW_WIDTH - 100), -20)
            
        elif self.state == GameState.INTRO:
            self.background.set_time("day")
            if random.random() < 0.2: self.particles.spawn_snow()
            self._handle_partner_movement(dt)
            if self.state_timer < 4: self.message = settings.INTRO_MESSAGE
            else: self.message = ""
            if self.state_timer > 8:
                self.state = GameState.WANDER
                self.state_timer = 0
                
        elif self.state == GameState.WANDER:
            self._handle_partner_movement(dt)
            if random.random() < 0.15: self.particles.spawn_snow()
            if random.random() < 0.1: self.particles.spawn_sparkle(self.partner.x + random.randint(-30, 30), self.partner.y + random.randint(-30, 30))
            self.thoughts.timer += dt
            if self.thoughts.timer > 4.0:
                self.thoughts.timer = 0
                self.thoughts.spawn_thought(self.partner.x, self.partner.y)
            if self.state_timer > 15:
                self.state = GameState.MEETING
                self.state_timer = 0
                self.dialogue.show("", settings.MEETING_MESSAGE, 3.0)
                
        elif self.state == GameState.MEETING:
            if self.player.x < self.partner.x - 120:
                self.player.x += 60 * dt
                self.player.facing_right = True
                self.player.walking = True
            else:
                self.player.walking = False
            if random.random() < 0.1: self.particles.spawn_snow()
            if self.state_timer > 6:
                self.state = GameState.CONVERSATION
                self.state_timer = 0
                self.dialogue.show(settings.PLAYER_NAME, settings.PLAYER_GREETING, 4.0)
                
        elif self.state == GameState.CONVERSATION:
            if random.random() < 0.08: self.particles.spawn_snow()
            if 4 <= self.state_timer < 4.1:
                self.dialogue.show(settings.PARTNER_NAME, settings.PARTNER_REPLY, 4.0)
            elif 9 <= self.state_timer < 9.1:
                self.dialogue.show(settings.PLAYER_NAME, settings.PLAYER_ADVICE, 4.0)
            elif 14 <= self.state_timer < 14.1:
                self.dialogue.show(settings.PARTNER_NAME, settings.PARTNER_AGREE, 3.0)
            if self.state_timer > 18:
                self.state = GameState.SLEEP_TRANSITION
                self.state_timer = 0
                
        elif self.state == GameState.SLEEP_TRANSITION:
            if self.state_timer > 2: self.partner.sleeping = True
            if random.random() < 0.15: self.particles.spawn_dream_particle()
            if 4 <= self.state_timer < 4.1: self.fading_out = True; self.fade_alpha = 0
            if self.state_timer > 6:
                self.state = GameState.SLEEP
                self.state_timer = 0
                self.background.set_time("evening")
                
        elif self.state == GameState.SLEEP:
            if self.player.x > -200:
                self.player.x -= 50 * dt
                self.player.facing_right = False
                self.player.walking = True
            if random.random() < 0.2: self.particles.spawn_dream_particle()
            if self.state_timer > 8:
                self.state = GameState.DREAM
                self.state_timer = 0
                self.background.set_time("dream")
                self.player.holding_rose = True
                self.player.x = -200
                self.fading_in = True; self.fade_alpha = 255
                
        elif self.state == GameState.DREAM:
            if random.random() < 0.3: self.particles.spawn_dream_particle()
            if random.random() < 0.1: self.particles.spawn_sparkle(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT))
            if random.random() < 0.15: self.particles.spawn_rose_petal()
            if self.state_timer > 10:
                self.state = GameState.WAKE_TRANSITION
                self.state_timer = 0
                self.background.set_time("evening")
                
        elif self.state == GameState.WAKE_TRANSITION:
            if self.player.x < self.partner.x - 100:
                self.player.x += 70 * dt
                self.player.facing_right = True
                self.player.walking = True
            else: self.player.walking = False
            if random.random() < 0.1: self.particles.spawn_rose_petal()
            if self.state_timer > 5:
                self.state = GameState.REVEAL
                self.state_timer = 0
                self.dialogue.show(settings.PLAYER_NAME, settings.REVEAL_MESSAGE, 5.0)
                
        elif self.state == GameState.REVEAL:
            if random.random() < 0.2: self.particles.spawn_rose_petal()
            if random.random() < 0.15: self.particles.spawn_sparkle(self.player.x + random.randint(-40, 40), self.player.y + random.randint(-40, 40))
            if self.state_timer > 3: self.partner.sleeping = False
            if self.state_timer > 8:
                self.state = GameState.KISS
                self.state_timer = 0
                
        elif self.state == GameState.KISS:
            if abs(self.player.x - self.partner.x) > 60: self.player.x += 30 * dt
            if 2 <= self.state_timer < 2.5:
                for _ in range(20):
                    angle = random.uniform(0, math.pi * 2)
                    speed = random.uniform(50, 150)
                    self.particles.particles.append(Particle(
                        x=self.partner.x + 20, y=self.partner.y - 20,
                        vx=math.cos(angle) * speed, vy=math.sin(angle) * speed - 50,
                        life=random.uniform(1.5, 3.0), max_life=3.0,
                        color=settings.HEART_RED, size=8, particle_type="heart"
                    ))
            if random.random() < 0.3: self.particles.spawn_heart(self.partner.x + random.randint(-50, 50), self.partner.y - random.randint(20, 60))
            if random.random() < 0.2: self.particles.spawn_rose_petal()
            if self.state_timer > 7:
                self.state = GameState.MARRIAGE
                self.state_timer = 0
                self.background.set_time("night")
                
        elif self.state == GameState.MARRIAGE:
            if random.random() < 0.5: self.particles.spawn_rose_petal()
            if random.random() < 0.4: self.particles.spawn_heart(random.randint(100, settings.WINDOW_WIDTH - 100), random.randint(-20, settings.WINDOW_HEIGHT // 2))
            if random.random() < 0.3: self.particles.spawn_sparkle(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT))
            if self.state_timer < 5: self.message = settings.MARRIAGE_MESSAGE_1
            elif self.state_timer < 10: self.message = settings.MARRIAGE_MESSAGE_2
            else: self.message = ""
            if self.state_timer > 12:
                self.state = GameState.END
                self.state_timer = 0
                
        elif self.state == GameState.END:
            if random.random() < 0.4: self.particles.spawn_rose_petal()
            if random.random() < 0.3: self.particles.spawn_heart(random.randint(100, settings.WINDOW_WIDTH - 100), random.randint(-20, settings.WINDOW_HEIGHT // 2))
            if random.random() < 0.2: self.particles.spawn_sparkle(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT))
            self.message = settings.FINAL_MESSAGE

    def _handle_partner_movement(self, dt: float):
        keys = pygame.key.get_pressed()
        speed = 80 * dt
        moved = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.partner.x -= speed
            self.partner.facing_right = False
            moved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.partner.x += speed
            self.partner.facing_right = True
            moved = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.partner.y -= speed
            moved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.partner.y += speed
            moved = True
        self.partner.walking = moved
        self.partner.x = max(50, min(settings.WINDOW_WIDTH - 150, self.partner.x))
        self.partner.y = max(settings.WINDOW_HEIGHT - 250, min(settings.WINDOW_HEIGHT - 100, self.partner.y))

    def update_fade(self, dt: float):
        if self.fading_out:
            self.fade_alpha += 150 * dt
            if self.fade_alpha >= 255: self.fade_alpha = 255; self.fading_out = False
        if self.fading_in:
            self.fade_alpha -= 150 * dt
            if self.fade_alpha <= 0: self.fade_alpha = 0; self.fading_in = False

    def render(self):
        self.background.draw(self.renderer.get_screen())
        self.particles.draw(self.renderer.get_screen(), foreground=False)
        if self.player.x > -100: self.player.draw(self.renderer.get_screen())
        self.partner.draw(self.renderer.get_screen())
        self.particles.draw(self.renderer.get_screen(), foreground=True)
        self.thoughts.draw(self.renderer.get_screen())
        self.dialogue.draw(self.renderer.get_screen())
        if self.message: self.draw_message()
        if self.state == GameState.TITLE: self.draw_title_screen()
        if self.fade_alpha > 0:
            fade_surf = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
            fade_surf.fill(settings.BLACK)
            fade_surf.set_alpha(int(self.fade_alpha))
            self.renderer.get_screen().blit(fade_surf, (0, 0))
        self.renderer.flip()

    def draw_message(self):
        font = self.font_end if self.state == GameState.END else self.font_msg
        words = self.message.split()
        lines = []
        curr = ""
        for w in words:
            if font.size(curr + w + " ")[0] < settings.WINDOW_WIDTH - 100: curr += w + " "
            else: lines.append(curr.strip()); curr = w + " "
        lines.append(curr.strip())
        
        y_off = 80
        for i, line in enumerate(lines):
            text = font.render(line, True, settings.WINE_RED)
            rect = text.get_rect(center=(settings.WINDOW_WIDTH // 2, y_off + i * 50))
            bg = rect.inflate(30, 15)
            for o in range(5, 0, -1):
                pygame.draw.rect(self.renderer.get_screen(), (255, 200, 200), bg.inflate(o*2, o*2), border_radius=10)
            pygame.draw.rect(self.renderer.get_screen(), settings.WHITE, bg, border_radius=10)
            pygame.draw.rect(self.renderer.get_screen(), settings.ROSE_RED, bg, 4, border_radius=10)
            self.renderer.get_screen().blit(text, rect)

    def draw_title_screen(self):
        overlay = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        overlay.fill(settings.BLACK)
        overlay.set_alpha(100)
        self.renderer.get_screen().blit(overlay, (0, 0))
        pulse = abs(math.sin(self.title_pulse * 2))
        color = (int(settings.ROSE_RED[0]*(0.7+0.3*pulse)), int(settings.ROSE_RED[1]*(0.7+0.3*pulse)), int(settings.ROSE_RED[2]*(0.7+0.3*pulse)))
        text = self.font_title.render("Mazyyy wali Gameee", True, color)
        rect = text.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 - 100))
        bg = rect.inflate(40, 20)
        pygame.draw.rect(self.renderer.get_screen(), settings.WHITE, bg, border_radius=15)
        pygame.draw.rect(self.renderer.get_screen(), settings.ROSE_RED, bg, 5, border_radius=15)
        self.renderer.get_screen().blit(text, rect)
        sub = self.font_subtitle.render("mazyy wali story", True, settings.WINE_RED)
        self.renderer.get_screen().blit(sub, sub.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 - 30)))
        if int(self.title_pulse * 2) % 2 == 0:
            p = self.font_prompt.render("Press SPACE or ENTER to begin", True, settings.SOFT_PINK)
            self.renderer.get_screen().blit(p, p.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 + 100)))
        for i in range(3):
            self.particles._draw_heart(self.renderer.get_screen(), settings.WINDOW_WIDTH//2 + (i-1)*100, settings.WINDOW_HEIGHT//2 + 180, 8, settings.HEART_RED, 1.0)
