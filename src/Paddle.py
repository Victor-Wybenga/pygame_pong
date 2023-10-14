import pygame
from Screen import screen

class Paddle(pygame.rect.Rect):
    def __init__(self, position: pygame.Vector2, up_key: pygame.key, down_key: pygame.key):
        self.size = (10, 100)
        self.center = position
        self.color = pygame.color.Color(255, 255, 255, 255)
        self.speed = 500
        self.up_key = up_key
        self.down_key = down_key
        self.score = 0
    def update(self, dt: float):
        if pygame.key.get_pressed()[self.up_key]:
            if self.top > 0:
                self.y += -self.speed * dt
        if pygame.key.get_pressed()[self.down_key]:
            if self.bottom < screen.get_height():
                self.y += self.speed * dt

left_paddle = Paddle((25, screen.get_height() / 2), pygame.K_w, pygame.K_s)
right_paddle = Paddle((screen.get_width() - 25, screen.get_height() / 2), pygame.K_i, pygame.K_k)