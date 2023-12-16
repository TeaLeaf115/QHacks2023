from sprite import Sprite

import pygame


class Entity(Sprite):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def movement(self):
        self.velocity += self.acceleration * 5

    def collision(self):
        pass

    def update(self):
        self.movement()

    