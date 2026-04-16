import pygame
from clock import prepare_hand, get_angles
import sys

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Hello Kitty Clock 🎀")
CENTER = (400, 400) # Центр для окна 800x800
clock = pygame.time.Clock()

# Загружаем фон
bg = pygame.image.load("images/mainclock.png").convert_alpha()
bg = pygame.transform.scale(bg, (800, 800))

# Загружаем твои фото
h_img_raw = pygame.image.load("images/hour.jpg").convert_alpha()
s_img_raw = pygame.image.load("images/second.jpg").convert_alpha()

# Если стрелки на экране СЛИШКОМ большие, раскомментируй эти две строки ниже:
# h_img_raw = pygame.transform.scale(h_img_raw, (40, 250))
# s_img_raw = pygame.transform.scale(s_img_raw, (20, 350))

# Подготавливаем их (делаем невидимую нижнюю часть)
h_hand = prepare_hand(h_img_raw)
s_hand = prepare_hand(s_img_raw)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем углы из clock.py
    h_ang, m_ang, s_ang = get_angles()

    # Рисуем
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    # Рисуем часовую (она на самом деле минутная у тебя в файлах, но не важно)
    rot_h = pygame.transform.rotate(h_hand, h_ang)
    rect_h = rot_h.get_rect(center=CENTER)
    screen.blit(rot_h, rect_h)

    # Рисуем секундную
    rot_s = pygame.transform.rotate(s_hand, s_ang)
    rect_s = rot_s.get_rect(center=CENTER)
    screen.blit(rot_s, rect_s)

    # ОБЯЗАТЕЛЬНО: Обновляем экран, иначе он будет черным!
    pygame.display.flip()
    
    # Ограничиваем скорость, чтобы не грузить процессор
    clock.tick(60)

pygame.quit()
sys.exit()