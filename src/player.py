from entity import Entity

import pygame


class Player(Entity):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

        self.max_velocity = 20

        # animation
        self.animation_cooldowns = {
            'run': 100,
            'dash': 100
        }

        self.animation_frames = {
            action: self.get_images(f'player/{action}', isFolder=True) 
            for action in self.animation_cooldowns
        }

    def movement(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        down = keys[pygame.K_s]
        up = keys[pygame.K_w]

        self.acceleration.xy = right - left, down - up

        if self.acceleration:
            self.acceleration.scale_to_length(self.max_velocity)
            self.velocity += self.acceleration
            self.velocity *= 0.5

        else:
            self.velocity *= 0.9

        super().movement()

    def collision(self):
        pass

    def update(self):
        self.movement()
        self.animation()
