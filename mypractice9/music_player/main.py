import pygame
import sys
from player import MusicPlayer

# Настройки окна
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Music Player")
    font = pygame.font.SysFont("Arial", 24)
    clock = pygame.time.Clock()

    # Путь к твоей папке с музыкой (как на скриншоте)
    player = MusicPlayer("music")

    running = True
    while running:
        screen.fill(WHITE)
        
        # Отображение информации
        status = "Playing" if player.is_playing else "Stopped"
        track_text = font.render(f"Track: {player.get_current_track_name()}", True, BLACK)
        status_text = font.render(f"Status: {status}", True, GREEN if player.is_playing else BLACK)
        
        controls_text = font.render("P: Play | S: Stop | N: Next | B: Back", True, (100, 100, 100))

        screen.blit(track_text, (20, 50))
        screen.blit(status_text, (20, 100))
        screen.blit(controls_text, (20, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # Play
                    player.play()
                elif event.key == pygame.K_s: # Stop
                    player.stop()
                elif event.key == pygame.K_n: # Next
                    player.next_track()
                elif event.key == pygame.K_b: # Back
                    player.prev_track()
                elif event.key == pygame.K_q: # Quit
                    running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()