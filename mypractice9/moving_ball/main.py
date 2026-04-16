import pygame
import sys
from ball import Ball

# Константы по заданию
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    # Создаем мяч в центре экрана
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, RED, WIDTH, HEIGHT)

    running = True
    while running:
        # 1. Фон всегда белый
        screen.fill(WHITE)

        # 2. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move("up")
                elif event.key == pygame.K_DOWN:
                    ball.move("down")
                elif event.key == pygame.K_LEFT:
                    ball.move("left")
                elif event.key == pygame.K_RIGHT:
                    ball.move("right")

        # 3. Отрисовка мяча
        ball.draw(screen)

        # 4. Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Ограничение FPS для плавности

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()