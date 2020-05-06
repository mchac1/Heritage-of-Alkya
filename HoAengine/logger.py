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

        # Création de la surface pygame
        if cts.size == "small":
            self.pygame_surface = pygame.Surface(cts.surface_size_small, cts.surface_flags)
            self.text_height = cts.font_small.render('A', True, (0, 0, 0)).get_height()
        elif cts.size == "medium":
            self.pygame_surface = pygame.Surface(cts.surface_size_medium, cts.surface_flags)
            self.text_height = cts.font_medium.render('A', True, (0, 0, 0)).get_height()
        else:
            self.pygame_surface = pygame.Surface(cts.surface_size_large, cts.surface_flags)
            self.text_height = cts.font_large.render('A', True, (0, 0, 0)).get_height()
        self.scroll = 0

    def log(self, level, message, thread="Main-Thread"):
        log = self.log_pattern.format(strftime("%H-%M-%S"), thread, level, message)
        print(log)
        self.logs.append((level, log))

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

    def get_pygame_surface(self):
        self.pygame_surface.fill(cts.bg_color)

        max_height = len(self.logs)*self.text_height
        if cts.size == "small":
            for i, log in enumerate(self.logs):
                level, msg = log
                text = cts.font_small.render(msg, True, cts.colors[level])
                self.pygame_surface.blit(text, (0, i*self.text_height))
            ratio = min(1, cts.surface_size_small[1]/max_height)
            pygame.draw.rect(self.pygame_surface, (200, 200, 200), (cts.surface_size_small[0]-20, 0, 20, cts.surface_size_small[1]))
            pygame.draw.rect(self.pygame_surface, (255, 255, 255), (cts.surface_size_small[0]-20, int(self.scroll*ratio), 20, int(cts.surface_size_small[1]*ratio)))
        elif cts.size == "medium":
            for i, log in enumerate(self.logs):
                level, msg = log
                text = cts.font_medium.render(msg, True, cts.colors[level])
                self.pygame_surface.blit(text, (0, i*self.text_height))
            ratio = max(1, cts.surface_size_medium[1]/max_height)
            pygame.draw.rect(self.pygame_surface, (200, 200, 200), (cts.surface_size_medium[0]-20, 0, 20, cts.surface_size_medium[1]))
            pygame.draw.rect(self.pygame_surface, (255, 255, 255), (cts.surface_size_medium[0]-20, int(self.scroll*ratio), 20, int(cts.surface_size_medium[1]*ratio)))
        else:
            for i, log in enumerate(self.logs):
                level, msg = log
                text = cts.font_large.render(msg, True, cts.colors[level])
                self.pygame_surface.blit(text, (0, i*self.text_height))
            ratio = max(1, cts.surface_size_medium[1]/max_height)
            pygame.draw.rect(self.pygame_surface, (200, 200, 200), (cts.surface_size_large[0]-20, 0, 20, cts.surface_size_large[1]))
            pygame.draw.rect(self.pygame_surface, (255, 255, 255), (cts.surface_size_large[0]-20, int(self.scroll*ratio), 20, int(cts.surface_size_large[1]*ratio)))

        return self.pygame_surface

