import pygame

class Ball:
    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = 20  # Шаг перемещения по заданию
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, direction):
        # Проверяем направление и не выйдет ли мяч за границы
        if direction == "up":
            if self.y - self.step >= self.radius:
                self.y -= self.step
        elif direction == "down":
            if self.y + self.step <= self.screen_height - self.radius:
                self.y += self.step
        elif direction == "left":
            if self.x - self.step >= self.radius:
                self.x -= self.step
        elif direction == "right":
            if self.x + self.step <= self.screen_width - self.radius:
                self.x += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)