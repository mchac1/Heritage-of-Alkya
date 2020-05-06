#! usr/bin/env python3
#-*- coding: utf-8 -*-

# importation des modules complémentaires nécéssaires
from HoAengine import constants as cts
import HoAengine
import os
import pygame

# initialisation du rendu pygame
os.environ["SDL_VIDEODRIVER"] = "directx" # use directx to enable hardware acceleration

pygame.init()

screen = pygame.display.set_mode(cts.WindowCts.size, cts.WindowCts.flags)

print("Video driver :", pygame.display.get_driver())
print("Video Infos :", pygame.display.Info())
