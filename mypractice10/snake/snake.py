import pygame
import random

class Snake:
    def __init__(self):
        self.size = 20

       
        self.body = [
            [100, 100],
            [80, 100],
            [60, 100]
        ]

        self.direction = "RIGHT"

    def move(self):
        head = self.body[0].copy()

        if self.direction == "RIGHT":
            head[0] += self.size
        if self.direction == "LEFT":
            head[0] -= self.size
        if self.direction == "UP":
            head[1] -= self.size
        if self.direction == "DOWN":
            head[1] += self.size

        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        
        self.body.append(self.body[-1])

    def check_collision_with_self(self):
       
        return self.body[0] in self.body[1:]

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        return False

    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (block[0], block[1], self.size, self.size))


class Food:
    def __init__(self, snake_body, width, height, size):
        self.size = size
        self.width = width
        self.height = height
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            x = random.randint(0, (self.width - self.size) // self.size) * self.size
            y = random.randint(0, (self.height - self.size) // self.size) * self.size

            if [x, y] not in snake_body:
                return [x, y]

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))