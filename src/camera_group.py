import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

    def render(self):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.sprite_layer):
            self.screen.blit(sprite.image, sprite.coords)

    def update(self):
        for sprite in self.sprites():
            sprite.update()        