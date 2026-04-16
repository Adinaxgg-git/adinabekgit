import pygame
import datetime

def prepare_hand(image):
    """Готовим фото к вращению: удваиваем высоту."""
    w, h = image.get_size()
    # Создаем прозрачную поверхность в два раза выше стрелки
    new_surf = pygame.Surface((w, h * 2), pygame.SRCALPHA)
    # Рисуем стрелку в ВЕРХНЕЙ части. 
    # Теперь геометрический центр всей этой картинки — это низ стрелки (кольцо).
    new_surf.blit(image, (0, 0))
    return new_surf

def get_angles():
    """Считаем время и переводим в градусы."""
    now = datetime.datetime.now()
    
    # Секунды: - потому что в Pygame rotate идет против часовой
    s_angle = -now.second * 6
    
    # Минуты
    m_angle = -now.minute * 6
    
    # Часы (плавное движение)
    h_angle = -((now.hour % 12) * 30 + now.minute / 2)
    
    return h_angle, m_angle, s_angle