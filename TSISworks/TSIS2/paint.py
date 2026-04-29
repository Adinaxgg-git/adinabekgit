import pygame
import sys
import math
import datetime
from collections import deque

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

clock = pygame.time.Clock()

# ---------- COLORS ----------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

current_color = BLACK
brush_size = 2

# ---------- CANVAS ----------
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# ---------- MODES ----------
mode = "pen"   # pen, line, text, fill, rect, circle, square, etc.

start_pos = None
prev_pos = None

# ---------- TEXT ----------
text_input = ""
text_pos = None
typing = False

font = pygame.font.SysFont("Arial", 24)

# ---------- FUNCTIONS ----------

def draw_line(a, b):
    pygame.draw.line(canvas, current_color, a, b, brush_size)


def flood_fill(x, y, target_color, replacement_color):

    if target_color == replacement_color:
        return

    queue = deque()
    queue.append((x,y))

    while queue:

        cx, cy = queue.popleft()

        if 0 <= cx < WIDTH and 0 <= cy < HEIGHT:

            if canvas.get_at((cx,cy)) == target_color:

                canvas.set_at((cx,cy), replacement_color)

                queue.append((cx+1,cy))
                queue.append((cx-1,cy))
                queue.append((cx,cy+1))
                queue.append((cx,cy-1))


def save_canvas():
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"paint_{now}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)


# ---------- MAIN LOOP ----------
running = True

while running:

    screen.blit(canvas, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------- KEYBOARD ----------
        if event.type == pygame.KEYDOWN:

            # tools
            if event.key == pygame.K_1:
                mode = "pen"

            if event.key == pygame.K_2:
                mode = "line"

            if event.key == pygame.K_3:
                mode = "fill"

            if event.key == pygame.K_4:
                mode = "text"

            # brush sizes
            if event.key == pygame.K_5:
                brush_size = 2

            if event.key == pygame.K_6:
                brush_size = 5

            if event.key == pygame.K_7:
                brush_size = 10

            # colors
            if event.key == pygame.K_r:
                current_color = RED

            if event.key == pygame.K_g:
                current_color = GREEN

            if event.key == pygame.K_b:
                current_color = BLUE

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

            # TEXT typing
            if typing:

                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text_input, True, current_color), text_pos)
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""

                else:
                    text_input += event.unicode


        # ---------- MOUSE ----------
        if event.type == pygame.MOUSEBUTTONDOWN:

            start_pos = event.pos

            # fill tool
            if mode == "fill":
                target = canvas.get_at(start_pos)
                flood_fill(start_pos[0], start_pos[1], target, current_color)

            # text tool
            if mode == "text":
                typing = True
                text_pos = start_pos


        if event.type == pygame.MOUSEBUTTONUP:

            end_pos = event.pos

            # LINE tool
            if mode == "line":
                draw_line(start_pos, end_pos)

            start_pos = None


    # ---------- PEN TOOL ----------
    if pygame.mouse.get_pressed()[0]:

        x,y = pygame.mouse.get_pos()

        if mode == "pen":
            if prev_pos:
                pygame.draw.line(canvas, current_color, prev_pos, (x,y), brush_size)

            prev_pos = (x,y)

    else:
        prev_pos = None


    # ---------- TEXT PREVIEW ----------
    if typing:
        preview = font.render(text_input, True, current_color)
        screen.blit(preview, text_pos)


    pygame.display.update()
    clock.tick(60)