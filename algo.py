#usr/bin/python3
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

game_run = True

while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            
        