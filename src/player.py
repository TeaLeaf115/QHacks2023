from entity import Entity

import pygame


class Player(Entity):
    def __init__(self, coords: tuple, size: tuple, game, groups):
        super().__init__(coords, size, game, groups)

        self.max_velocity = 10
        self.jumping = False

        # animation
        self.animation_cooldowns = {
            'run': 100,
            'dash': 100
        }

        self.animation_frames = {
            action: self.get_images(f'player/{action}', isFolder=True) 
            for action in self.animation_cooldowns
        }

        self.image = self.animation_frames[self.action][self.frame]
        

    def movement(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]

        space = keys[pygame.K_SPACE]

        self.acceleration.x = right - left

        if self.acceleration.x:
            self.acceleration.x *= self.max_velocity
            self.velocity.x += self.acceleration.x
            self.velocity.x *= 0.5

        else:
            self.velocity.x *= 0.9

        if space:
            self.velocity.y = -20

        ground_y = self.game.height * 2 / 3
        if self.coords.y < ground_y:
            self.velocity.y += 2
        
        if self.coords.y > ground_y:
            self.coords.y = ground_y

        super().movement()

    def collision(self):
        pass

    def check_state(self):
        if abs(self.velocity.x) > self.max_velocity * 2 / 3:
            self.action = 'dash'

        else:
            self.action = 'run'

    def update(self):
        self.movement()
        self.check_state()
        self.animation()
