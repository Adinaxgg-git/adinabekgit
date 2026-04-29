import pygame
import random
import sys

from player import Player
from coin import Coin


pygame.init()

WIDTH=400
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Racer")

FPS=60
clock=pygame.time.Clock()


# ---------- Road scrolling ----------
road=pygame.image.load("street.png")
road=pygame.transform.scale(road,(400,600))

road_y1=0
road_y2=-600

scroll_speed=5


# ---------- Enemy ----------
enemy_img=pygame.image.load("enemy.png")
enemy_img=pygame.transform.scale(enemy_img,(50,100))

enemy_rect=enemy_img.get_rect()
enemy_rect.center=(random.randint(80,320),0)

enemy_speed=5


# ---------- Player ----------
player=Player()


# ---------- Coin ----------
coin=Coin()


font=pygame.font.SysFont("Arial",30)

score=0


running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    # ---------- Moving road ----------
    road_y1 += scroll_speed
    road_y2 += scroll_speed

    if road_y1 >= 600:
        road_y1=-600

    if road_y2 >=600:
        road_y2=-600


    screen.blit(road,(0,road_y1))
    screen.blit(road,(0,road_y2))


    # ---------- Player movement ----------
    player.move()
    screen.blit(player.image,player.rect)


    # ---------- Enemy movement ----------
    enemy_rect.move_ip(0,enemy_speed)

    if enemy_rect.top>600:
        enemy_rect.center=(
            random.randint(80,320),
            0
        )

    screen.blit(enemy_img,enemy_rect)


    # ---------- Coin movement ----------
    coin.move()

    screen.blit(
        coin.image,
        coin.rect
    )


    # Show coin weight above coin
    weight_text=font.render(
        str(coin.value),
        True,
        (255,255,0)
    )

    screen.blit(
        weight_text,
        (coin.rect.x,coin.rect.y-25)
    )


    # ---------- Collect coin ----------
    if player.rect.colliderect(coin.rect):

        score+=coin.value

        coin.reset()


        # Increase enemy speed every 10 points
        if score%10==0:
            enemy_speed+=1


    # ---------- Crash ----------
    if player.rect.colliderect(enemy_rect):

        print("Game Over")
        pygame.quit()
        sys.exit()


    # ---------- Score top right ----------
    score_text=font.render(
        f"Coins: {score}",
        True,
        (255,255,255)
    )

    screen.blit(score_text,(240,20))


    pygame.display.update()
    clock.tick(FPS)