import pygame
import random

WIDTH, HEIGHT = 600, 600


class Snake:

    def __init__(self):
        self.body = [[100,100],[90,100],[80,100]]
        self.dir = "RIGHT"
        self.change = "RIGHT"

    def move(self):

        self.dir = self.change
        head = self.body[0].copy()

        if self.dir == "RIGHT":
            head[0] += 10
        if self.dir == "LEFT":
            head[0] -= 10
        if self.dir == "UP":
            head[1] -= 10
        if self.dir == "DOWN":
            head[1] += 10

        self.body.insert(0, head)
        self.body.pop()


class Food:

    def __init__(self):
        self.pos = [random.randrange(1,59)*10, random.randrange(1,59)*10]
        self.value = random.choice([1,2,3,5])
        self.spawn_time = pygame.time.get_ticks()

    def respawn(self):
        self.pos = [random.randrange(1,59)*10, random.randrange(1,59)*10]
        self.value = random.choice([1,2,3,5])
        self.spawn_time = pygame.time.get_ticks()


class Poison:

    def __init__(self):
        self.pos = [random.randrange(1,59)*10, random.randrange(1,59)*10]


class PowerUp:

    def __init__(self):
        self.type = random.choice(["speed","slow","shield"])
        self.pos = [random.randrange(1,59)*10, random.randrange(1,59)*10]
        self.spawn_time = pygame.time.get_ticks()


class Obstacle:

    def __init__(self):
        self.blocks = []
        self.generate()

    def generate(self):
        self.blocks = []

        for _ in range(5):
            x = random.randrange(1,59)*10
            y = random.randrange(1,59)*10
            self.blocks.append([x,y])