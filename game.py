#! usr/bin/env python3
# -*- coding:utf-8 -*-

# importation des modules complémentaires nécéssaires
from HoAengine import constants as cts
from HoAengine.logger import Logger
import os
import pygame

# initialisation du rendu pygame
os.environ["SDL_VIDEODRIVER"] = "directx"  # use directx to enable hardware

pygame.init()
pygame.display.get_driver()

# Création des composants du jeu
screen = pygame.display.set_mode(cts.WindowCts.size, cts.WindowCts.flags, cts.WindowCts.depth)
logger = Logger()
# logger.log("Warning", "Hello World !")

pygame.display.set_caption(cts.WindowCts.title)

running = True
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
fps = 120
try:
    while running:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT + 1:
                fps = clock.get_fps()
                pygame.display.set_caption(cts.WindowCts.title + " | " + str(int(fps)))
                logger.log("Info", "FPS updated")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((155, 255, 55))
        screen.blit(logger.surface, logger.surface.get_rect(bottomleft=(0, cts.WindowCts.size[1])))
        pygame.display.flip()

    pygame.quit()
except Exception as e:
    pygame.quit()
    raise e
