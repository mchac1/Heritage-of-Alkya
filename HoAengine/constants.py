# -*- coding:utf-8 -*-

# Importation des modules complémentaires nécéssaires
from pygame.constants import HWSURFACE, DOUBLEBUF, HWACCEL, SRCALPHA
from pygame.font import SysFont, init  # , Font
from os.path import join

# Initialisation des composants
init()


# Création des variables système
class SystemCts:
    """
    Constantes liées au système
    """
    log = True


# Création des variables du logger
class LoggerCts:
    """
    Constantes liées au logger
    """
    size = "medium"
    folder = join("HoAdata", "logs")
    colors = {
        "Debug": (75, 75, 75),
        "Info": (255, 255, 255),
        "Warning": (255, 155, 0),
        "Error": (255, 0, 0)
    }
    bg_color = (0, 0, 0, 175)
    font = {
        "small": SysFont("Courier", 10),
        "medium": SysFont("Courier", 15),
        "large": SysFont("Courier", 20)
    }
    surface_size = {
        "small": (400, 200),
        "medium": (600, 300),
        "large": (800, 400)
    }
    surface_flags = HWSURFACE | SRCALPHA | HWACCEL


# Création des variables de la fenêtre
class WindowCts:
    """
    Constantes liées à la fenêtre
    """
    size = (1000, 700)  # px (0, 0) = current resolution
    title = "The Heritage of Alkya"
    max_framerate = 120  # fps
    flags = HWSURFACE | DOUBLEBUF | HWACCEL  # | FULLSCREEN
    depth = 16


# Création des variables de la map
class MapCts:
    """
    Constantes liées à la map
    """
    tile_size = 32  # px
    tileset_folder = join("HoAassets", "Tilesets")
