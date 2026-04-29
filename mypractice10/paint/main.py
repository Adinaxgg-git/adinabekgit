import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLACK
tool = "brush"

drawing = False
start = (0,0)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:

            # инструменты
            if event.key == pygame.K_b:
                tool = "brush"

            if event.key == pygame.K_r:
                tool = "rectangle"

            if event.key == pygame.K_c:
                tool = "circle"

            if event.key == pygame.K_e:
                tool = "eraser"


            # цвета
            if event.key == pygame.K_1:
                color = BLACK

            if event.key == pygame.K_2:
                color = RED

            if event.key == pygame.K_3:
                color = BLUE



        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start = event.pos



        if event.type == pygame.MOUSEBUTTONUP:

            end = event.pos

            if tool == "rectangle":

                x = start[0]
                y = start[1]

                w = end[0]-start[0]
                h = end[1]-start[1]

                pygame.draw.rect(
                    screen,
                    color,
                    (x,y,w,h),
                    3
                )


            if tool == "circle":

                radius = abs(end[0]-start[0])

                pygame.draw.circle(
                    screen,
                    color,
                    start,
                    radius,
                    3
                )

            drawing = False



    if drawing:

        if tool == "brush":
            pygame.draw.circle(
                screen,
                color,
                pygame.mouse.get_pos(),
                4
            )


        if tool == "eraser":
            pygame.draw.circle(
                screen,
                WHITE,
                pygame.mouse.get_pos(),
                12
            )


    pygame.display.update()


pygame.quit()