from constants import *

import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(groups)
        self.game = game

        self.coords = pygame.math.Vector2(*coords)
        self.size = pygame.math.Vector2(*size)

        # images and rects
        self.image = pygame.Surface(size)
        self.image.fill(Color.BLUE)
        self.rect = self.image.get_rect(topleft=coords)

        # render
        self.sprite_layer = 0

        # animation
        self.frame = 0

    def get_images(self, filepath: str, isFolder=False):
        images = []
        if isFolder:
            # sorts filenames by length and then alphabetically
            filepaths = os.listdir(f'{SPRITE_PATH}/{filepath}')
            filepaths.sort(key=lambda filename: (len(filename), filename))

            for path in filepaths:
                filename = path[:-4].split('/')[-1]
                image = IMAGES[filename].copy()
                image = pygame.transform.scale(
                    image,
                    self.size
                )

                images.append(image)

        else:
           # filepath is a single image instead of a sprite folder
            filename = filepath.split('/')[-1]
            image = IMAGES[filename].copy()
            image = pygame.transform.scale(image, self.size)

            images.append(image)

        return images
    
        

    def update(self):
        pass
