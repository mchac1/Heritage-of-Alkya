# -*- coding:utf-8 -*-

# Importation des modules du package
from .constants import LoggerCts as cts
from .constants import SystemCts as output

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
        if output.log:
            print(log)
        self.logs.append((level, log))

        self.surface.fill(cts.bg_color)
        for i in range(min(len(self.logs), cts.surface_size[cts.size][1] // self.char_height)):
            text = cts.font[cts.size].render(self.logs[-i - 1][1], True, cts.colors[self.logs[-i - 1][0]])
            self.surface.blit(text, text.get_rect(bottomleft=(5, cts.surface_size[cts.size][1] - i * self.char_height - 5)))

    def save(self):
        filename = join(cts.folder, "Log of {}.log".format(strftime("%Y-%m-%d")))
        with open(filename, "w") as file:
            for _, log in self.logs:
                file.write(log + "\n")
            file.close()

    def load(self):
        filename = join(cts.folder, "Log of {}.log".format(strftime("%Y-%m-%d")))
        with open(filename, "w") as file:
            for line in file:
                level = line.split("]")[2][1:]
                self.logs.append((level, line[:-1]))
            file.close()
