import pygame
from os import path
from Paddle import left_paddle, right_paddle
from Ball import ball
from Screen import screen

def main():
    pygame.init()

    clock: pygame.time = pygame.time.Clock()
    running: bool = True
    paused: bool = False

    paused_text: str = "[PAUSED]"
    paused_sub_text: str = ""

    font_path: str = path.join("..", "assets", "font.ttf")
    font: pygame.font = pygame.font.Font(font_path, 96)
    sub_font: pygame.font = pygame.font.Font(font_path, 48)

    while running:
        dt: float = clock.tick(60) / 1000

        # events #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    paused_text = "[PAUSED]"
                    paused_sub_text = ""

        # update #
        if not paused:
            left_paddle.update(dt)
            right_paddle.update(dt)
            ball.update(dt)

        # render #
        screen.fill(pygame.Color(0, 0, 0, 255))

        screen.blit(
            font.render(f"P1: {left_paddle.score}", True, pygame.Color(180, 180, 180, 255)), 
            (50, 10)
        )
        screen.blit(
            font.render(f"P2: {right_paddle.score}", True, pygame.Color(180, 180, 180, 255)), 
            (screen.get_width() - 280, 10)
        )

        if paused:
            screen.blit(
                font.render(paused_text, True, pygame.Color(180, 180, 180, 255)), 
                (screen.get_width() / 2 - 200, screen.get_height() / 2 - 100)
            )
            screen.blit(
                sub_font.render(paused_sub_text, True, pygame.Color(180, 180, 180, 255)), 
                (screen.get_width() / 2 - 300, screen.get_height() / 2 + 10)
            )

        pygame.draw.rect(screen, left_paddle.color, left_paddle)
        pygame.draw.rect(screen, right_paddle.color, right_paddle)
        pygame.draw.rect(screen, ball.color, ball)

        if left_paddle.score >= 3:
            paused = True
            paused_text = "[P1 WINS]"
            paused_sub_text = "Press [SPACE] to restart"
            left_paddle.score = 0
            right_paddle.score = 0
        
        if right_paddle.score >= 3:
            paused = True
            paused_text = "[P2 WINS]"
            paused_sub_text = "Press [SPACE] to restart"
            left_paddle.score = 0
            right_paddle.score = 0
         
        pygame.display.flip()

if __name__ == "__main__":
    main()