from constants import *
from entity import Entity

import pygame
import random


class Player(Entity):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

        self.max_velocity = 5
        self.jump_velocity = 15
        self.jumping = False

        # animation
        self.animation_cooldowns = {
            'run': 100,
            'dash': 50
        }

        self.animation_frames = {
            action: self.get_images(f'player/{action}', isFolder=True) 
            for action in self.animation_cooldowns
        }

        self.image = self.animation_frames[self.action][self.frame]
        

    def movement(self):
        keys = pygame.key.get_pressed()
        
        # horizontal movement
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        self.acceleration.x = right - left

        if self.acceleration.x:
            self.acceleration.x *= self.max_velocity
            self.velocity.x += self.acceleration.x
            self.velocity.x *= 0.5

        elif not self.jumping:
            self.velocity.x *= 0.9

        # jump
        space = keys[pygame.K_SPACE]
        
        if space and not self.jumping:
            self.velocity.x = signum(self.velocity.x) * self.jump_velocity
            self.velocity.y = -self.jump_velocity

        # gravity
        ground_y = self.game.height * 2 / 3
        if self.coords.y < ground_y:
            self.velocity.y += gravity_acceleration
            self.jumping = True
        
        if self.coords.y > ground_y:
            self.coords.y = ground_y
            self.jumping = False

        # movement decay
        super().movement()

    def collision(self):
        pass

    def check_state(self):
        if abs(self.velocity.x) > self.max_velocity - 1:
            self.action = 'dash'

        else:
            self.action = 'run'

    def update(self):
        self.movement()
        self.check_state()
        self.animation()
