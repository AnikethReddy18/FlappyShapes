import pygame
from pygame import (K_UP,
                    K_DOWN,
                    K_LEFT,
                    K_RIGHT,
                    K_ESCAPE,
                    KEYDOWN,
                    QUIT, )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((0, 0, 255))
        self.surf_location = ((500 - 100) / 2, (650 - 100) / 2)
        self.rect = self.surf.get_rect()


pygame.init()

screen = pygame.display.set_mode([500, 650])

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(player.surf, player.surf_location)
    pygame.display.flip()

pygame.quit()
