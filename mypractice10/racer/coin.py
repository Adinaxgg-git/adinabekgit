import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загружаем картинку
        img = pygame.image.load("coin.png")
        # ИЗМЕНЯЕМ РАЗМЕР: 30 на 30 пикселей (можешь поменять цифры)
        self.image = pygame.transform.scale(img, (30, 30))
        
        self.rect = self.image.get_rect()
        # Появляется в случайном месте наверху
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        self.rect.move_ip(0, 5) 
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)