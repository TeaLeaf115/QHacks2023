from sprite import Sprite

import pygame


class Entity(Sprite):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)
        self.action = 'run'

        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

        self.animation_cooldowns = {
            'run': 100,
            'dash': 100
        }

        self.animation_frames = {action: [] for action in self.animation_cooldowns}
        self.animation_time = pygame.time.get_ticks()

    def movement(self):
        self.velocity += self.acceleration

    def collision(self):
        pass

    def check_state(self):
        if self.velocity.magnitude() > 2:
            self.action = 'dash'

        else:
            self.aciton = 'run'

    def animation(self):
        if self.frame >= len(self.animation_frames[self.action]):
            self.frame = 0
        
        if self.frame < len(self.animation_frames[self.action]):
            self.image = self.animation_frames[self.frame]

            # determines whether the animation cooldown is over
            if (self.animation_cooldown
                    and pygame.time.get_ticks() - self.animation_time > self.animation_cooldown[self.action]):

                self.animation_time = pygame.time.get_ticks()
                self.frame += 1

    def update(self):
        self.movement()

    