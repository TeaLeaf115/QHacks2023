from sprite import Sprite

import pygame


class Entity(Sprite):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

    def movement(self):
        pass

    def collision(self):
        pass

    def update(self):
        pass