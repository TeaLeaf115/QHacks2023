from sprite import Sprite

import pygame


class Entity(Sprite):
    def __init__(self, coords: tuple, size: tuple, groups: pygame.sprite.Group, game):
        super.__init__(coords, size, groups, game)

    def movement(self):
        pass

    def collision(self):
        pass

    def update(self):
        pass