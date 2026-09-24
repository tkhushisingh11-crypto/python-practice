import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]
direction = (GRID, 0)

food = (
    random.randrange(0, WIDTH, GRID),
    random.randrange(0, HEIGHT, GRID)
)

score = 0
font = pygame.font.SysFont(None, 30)

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID):
                direction = (0, -GRID)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID):
                direction = (0, GRID)
            elif event.key == pygame.K_LEFT and direction != (GRID, 0):
                direction = (-GRID, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID, 0):
                direction = (GRID, 0)

    head = (
        snake[0][0] + direction[0],
        snake[0][1] + direction[1]
    )

    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake
    ):
        break

    snake.insert(0, head)

    if head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, GRID),
            random.randrange(0, HEIGHT, GRID)
        )
    else:
        snake.pop()

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (*food, GRID, GRID))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID, GRID))

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()

print("Game Over!")
print("Final Score:", score)