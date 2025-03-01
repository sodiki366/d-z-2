import random
from all_colors import *
import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 720
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = WHITE
screen.fill(BACKGROUND)
x = 0
y = 0
rect_size = 200
center_x = WIDTH // 2
center_y = HEIGHT // 2
initial_size = 400
colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL,
          SILVER, GOLD]


FPS = 60
clock = pygame.time.Clock()
timer = 0
running = True
while running:
    # Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    size = 400
    for _ in range(19):
        pygame.draw.rect(screen, random.choice(COLORS), (WIDTH // 2 - size // 2, HEIGHT // 2 - size // 2, size, size),
                         2)
        size -= 10

    #
    #
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

