import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Загружаем твою картинку
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Начальная позиция
        self.rect.center = (160, 520) 
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Движение влево (не выходя за границы экрана)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        # Движение вправо (экран 400px в ширину)
        if self.rect.right < 400:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)