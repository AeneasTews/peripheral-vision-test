import time

import pygame
from screeninfo import get_monitors
from random import random, randrange

pygame.init()

led_size = 10
offset = -50

monitor = get_monitors()[0]
monitor.width += offset
monitor.height += offset
screen = pygame.display.set_mode((monitor.width, monitor.height))
clock = pygame.time.Clock()

running = True

led_timer = pygame.USEREVENT + 1
pygame.time.set_timer(led_timer, 1000)

rand_timer = pygame.USEREVENT + 1
pygame.time.set_timer(rand_timer, 500)
shownTime = time.time()

led_rect = pygame.rect.Rect(monitor.width // 2 - led_size, monitor.height // 2 - led_size, 2 * led_size, 2 * led_size)
rand_rect = pygame.rect.Rect(monitor.width // 2 - led_size, monitor.height // 2 - led_size, 2 * led_size, 2 * led_size)

led_counter = 0
rand_counter = 0
hit_counter = 0

while running:

    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == led_timer:
            if random() < 0.5:
                pygame.draw.rect(screen, (255, 0, 0), led_rect)
                led_counter += 1

        if event.type == rand_timer:
            if random() < 0.1:
                rand_rect.x = randrange(0, monitor.width - 2 * led_size)
                rand_rect.y = randrange(0, monitor.height - 2 * led_size)
                pygame.draw.rect(screen, (0, 255, 0), rand_rect)
                shownTime = time.time()
                rand_counter += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if time.time() - shownTime < 0.5:
                    hit_counter += 1

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

print(f"{led_counter} distractor blinks were shown")
print(f"{rand_counter} target blinks were shown")
print(f"{hit_counter} target blinks were registered")
