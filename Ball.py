import pygame
from Screen import screen
from Paddle import left_paddle, right_paddle

class Ball(pygame.rect.Rect):
    def __init__(self, position: pygame.Vector2):
        self.size = (10, 10)
        self.center = position
        self.color = pygame.color.Color(255, 255, 255, 255)
        self.speed = 400
        self.direction = pygame.Vector2(1, 1).normalize()

    def update(self, dt: float):
        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt
        self.speed += 5 * dt
        if self.top < 0 or self.bottom > screen.get_height():
            self.direction.y *= -1

        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            self.direction.x *= -1

        if ball.left < 0:
            self.center = (screen.get_width() / 2, screen.get_height() / 2)
            self.direction = pygame.Vector2(1, 1).normalize()
            self.speed = 400
            right_paddle.score += 1

        if ball.right > screen.get_width():
            self.center = (screen.get_width() / 2, screen.get_height() / 2)
            self.direction = pygame.Vector2(-1, 1).normalize()
            self.speed = 400
            left_paddle.score += 1
        

ball = Ball((screen.get_width() / 2, screen.get_height() / 2))