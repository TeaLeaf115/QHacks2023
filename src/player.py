from entity import Entity

import pygame


class Player(Entity):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def movement(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        down = keys[pygame.K_s]
        up = keys[pygame.K_w]
        
        self.acceleration.xy = right - left, down - up

        self.velocity += self.acceleration
        self.coords += self.velocity

    def collision(self):
        pass

    def update(self):
        self.movement()