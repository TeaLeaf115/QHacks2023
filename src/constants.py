from color import Color

import pygame
import os

pygame.init()
pygame.display.init()
pygame.display.set_mode()

# tile pixel size
TILE_SIZE = 100

# file paths
SPRITE_PATH = '../res'

# retrieving image files for tooltips
IMAGES = {}
for (path, dirs, files) in os.walk(SPRITE_PATH, topdown=True):
    for file in files:
        file_name, extension = file.split('.')
        if extension == 'png':
            IMAGES[file_name] = pygame.image.load(
                os.path.join(path, file)
            ).convert_alpha()
