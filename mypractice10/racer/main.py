import pygame, sys
from pygame.locals import *
import random, time
from player import Player
from coin import Coin

# Инициализация игры
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SCORE = 0

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60) # Шриф для Game Over

# Создание экрана
DISPLAYSURFACE = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer Game")

# Фон трассы
background = pygame.image.load("AnimatedStreet.png")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        img = pygame.image.load("Enemy.png")
        # Масштабируем врага, чтобы он не был на весь экран
        self.image = pygame.transform.scale(img, (50, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0) 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

# Создаем объекты
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группируем спрайты для удобства
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Рисуем фон
    DISPLAYSURFACE.blit(background, (0, 0))
    
    # Счётчик монет в углу
    scores = font.render("Coins: " + str(COIN_SCORE), True, WHITE)
    DISPLAYSURFACE.blit(scores, (280, 10))

    # Двигаем и рисуем всех (Игрока, Врага, Монету)
    for entity in all_sprites:
        DISPLAYSURFACE.blit(entity.image, entity.rect)
        entity.move()

    # Если подобрали монетку
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1
        # Возвращаем монету наверх
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, 360), 0)

    # Если врезались во врага
    if pygame.sprite.spritecollideany(P1, enemies):
        # Заливаем экран черным (или красным)
        DISPLAYSURFACE.fill(RED)
        
        # Создаем надпись GAME OVER
        game_over = font_big.render("GAME OVER", True, BLACK)
        # Центрируем надпись
        DISPLAYSURFACE.blit(game_over, (30, 250))
        
        pygame.display.update()
        
        # Ждем 2 секунды и закрываем игру
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
    pygame.time.Clock().tick(60)