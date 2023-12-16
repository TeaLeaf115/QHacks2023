import pygame

class Sprite(pygame.sprite.Sprite):
    def __init_(self, coords: tuple, size: tuple, groups: pygame.sprite.Group, game):
        super().__init__()
        self.game = game

        self.coords = pygame.math.Vector2(*coords)
        self.size = pygame.math.Vector2(*size)

        # images and rects
        self.image = pygame.Surface(size)
        self.rect = self.image.getRect(topleft=coords)

        # render
        self.sprite_layer = 0

        # animation
        self.frame = 0
    