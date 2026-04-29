import pygame
from snake import Snake, Food

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake = Snake()
food = Food(snake.body, WIDTH, HEIGHT, snake.size)

score = 0
level = 1
speed = 5

font = pygame.font.SysFont("Arial", 20)

running = True

while running:
    clock.tick(speed)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            if event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"


    snake.move()


    if snake.check_wall_collision(WIDTH, HEIGHT):
        print("Game Over (wall)")
        running = False

    if snake.check_collision_with_self():
        print("Game Over (self)")
        running = False


    if snake.body[0] == food.position:
        snake.grow()
        score += 1


        food = Food(snake.body, WIDTH, HEIGHT, snake.size)


        if score % 3 == 0:
            level += 1
            speed += 1   


    screen.fill((0, 0, 0))

    snake.draw(screen)
    food.draw(screen)


    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()