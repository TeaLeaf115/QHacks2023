from constants import *
from player import Player
from camera_group import CameraGroup

import pygame


class App:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('QuHacks')

        pygame.font.init()

        display_info = pygame.display.Info()
        self.width, self.height = display_info.current_w, display_info.current_h
        self.resolution = self.width, self.height

        self.screen = pygame.display.set_mode(
            self.resolution,
            pygame.DOUBLEBUF | pygame.FULLSCREEN
        )

        self.clock = pygame.time.Clock()
        self.runtime = True

        # groups
        self.camera_group = CameraGroup()
        self.player = Player((400, 400), (TILE_SIZE, ) * 2, self, self.camera_group)
        
    def run(self):
        while self.runtime:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.runtime = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.runtime = False

            self.draw()
            self.update()

            # updates screen
            pygame.display.update()
            self.clock.tick(60)

        # closes pygame application
        pygame.font.quit()
        pygame.display.quit()
        pygame.quit()

    def draw(self):
        self.screen.fill(Color.RED)

        self.camera_group.render()

    def update(self):
        self.camera_group.update()


if __name__ == '__main__':
    App().run()
