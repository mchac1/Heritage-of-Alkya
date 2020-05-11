#-*- coding: utf-8 -*-

# Importation des modules du package
from .constants import LoggerCts as cts

# Importation des modules complémentaires
from os.path import join
import pygame
from time import strftime

# Création du logger
class Logger:
    """
    Logger instance
    """
    def __init__(self):
        # Création des contenants
        self.logs = []

        # Création du patterne
        self.log_pattern = "[{}][{}][{}]: {}"

        # Création des attributs de taille
        self.char_height = cts.font[cts.size].render('A', True, (0, 0, 0)).get_height()

        # Création de la surface pygame
        self.surface = pygame.Surface(cts.surface_size[cts.size], cts.surface_flags)
        self.surface.fill(cts.bg_color)

    def log(self, level, message, thread="Main-Thread"):
        log = self.log_pattern.format(strftime("%H-%M-%S"), thread, level, message)
        print(log)
        self.logs.append((level, log))

        old = self.surface.convert_alpha()
        self.surface.fill(cts.bg_color)
        self.surface.blit(old, (0, -self.char_height))
        self.surface.blit(cts.font[cts.size].render(log, True, cts.colors[level]), (5, self.surface_size[self.size][1]-5))

    def save(self):
        filename = join(cts.folder, "Log of {}.log".format(strftime("%Y-%m-%d")))
        with open(filename, "w") as file:
            for _, log in self.logs:
                file.write(log+"\n")
            file.close()

    def load(self):
        filename = join(cts.folder, "Log of {}.log".format(strftime("%Y-%m-%d")))
        with open(filename, "w") as file:
            for line in file:
                level = line.split("]")[2][1:]
                self.logs.append((level, line[:-1]))
            file.close()

