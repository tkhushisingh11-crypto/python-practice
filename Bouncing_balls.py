import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

clock = pygame.time.Clock()

balls = []

for i in range(15):
    balls.append({
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "dx": random.choice([-4, -3, 3, 4]),
        "dy": random.choice([-4, -3, 3, 4]),
        "r": random.randint(15, 30),
        "color": (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
    })

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 30))

    for ball in balls:
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]

        if ball["x"] <= ball["r"] or ball["x"] >= WIDTH - ball["r"]:
            ball["dx"] *= -1

        if ball["y"] <= ball["r"] or ball["y"] >= HEIGHT - ball["r"]:
            ball["dy"] *= -1

        pygame.draw.circle(
            screen,
            ball["color"],
            (ball["x"], ball["y"]),
            ball["r"]
        )

    pygame.display.flip()

pygame.quit()