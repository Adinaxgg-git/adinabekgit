import pygame
import sys
import random

from game import Snake, Food, Poison, PowerUp, Obstacle
from db import init_db, save_game, leaderboard, personal_best

pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

init_db()

# ---------- STATE ----------
state = "menu"
username = ""

snake = Snake()
food = Food()
poison = Poison()
power = PowerUp()
obstacle = Obstacle()

score = 0
level = 1
speed = 10

active_power = None
power_start = 0


# ---------- MENU ----------
def draw_menu():

    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial",30)

    screen.blit(font.render("ENTER NAME + ENTER",True,(255,255,255)),(120,200))
    screen.blit(font.render(username,True,(0,255,0)),(250,300))


# ---------- GAME ----------
def draw_game():

    global score, level, speed, state

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.change = "LEFT"
    if keys[pygame.K_RIGHT]:
        snake.change = "RIGHT"
    if keys[pygame.K_UP]:
        snake.change = "UP"
    if keys[pygame.K_DOWN]:
        snake.change = "DOWN"


    snake.move()

    head = snake.body[0]

    # ---------- WALL ----------
    if head[0] < 0 or head[0] > 590 or head[1] < 0 or head[1] > 590:
        save_game(username, score, level)
        state = "gameover"

    # ---------- OBSTACLE ----------
    for b in obstacle.blocks:
        if head == b:
            save_game(username, score, level)
            state = "gameover"


    # ---------- FOOD ----------
    if head == food.pos:
        score += food.value
        snake.body.append(snake.body[-1])
        food.respawn()

        if score // 5 + 1 > level:
            level += 1
            speed += 1

            if level >= 3:
                obstacle.generate()


    # ---------- POISON ----------
    if head == poison.pos:
        snake.body = snake.body[:-2]

        if len(snake.body) <= 1:
            save_game(username, score, level)
            state = "gameover"


    # ---------- DRAW ----------
    for b in snake.body:
        pygame.draw.rect(screen,(0,255,0),(*b,10,10))

    pygame.draw.circle(screen,(255,255,0),food.pos,5)
    pygame.draw.rect(screen,(255,0,0),(*poison.pos,10,10))

    for ob in obstacle.blocks:
        pygame.draw.rect(screen,(100,100,100),(*ob,10,10))


    font = pygame.font.SysFont("Arial",20)
    screen.blit(font.render(f"Score:{score} Level:{level}",True,(255,255,255)),(10,10))


# ---------- LEADERBOARD ----------
def draw_leaderboard():

    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial",20)

    data = leaderboard()

    y = 100
    for i,d in enumerate(data):
        screen.blit(font.render(f"{i+1}. {d[0]} {d[1]} lvl {d[2]}",True,(255,255,255)),(100,y))
        y += 30


# ---------- GAME LOOP ----------
running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == "menu":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    state = "game"

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    username += event.unicode


        if state == "gameover":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_m:
                    state = "menu"
                    snake = Snake()
                    score = 0


    # ---------- STATES ----------
    if state == "menu":
        draw_menu()

    elif state == "game":
        draw_game()

    elif state == "leaderboard":
        draw_leaderboard()

    elif state == "gameover":
        screen.fill((0,0,0))
        font = pygame.font.SysFont("Arial",40)
        screen.blit(font.render("GAME OVER",True,(255,0,0)),(180,250))


    pygame.display.update()
    clock.tick(speed)