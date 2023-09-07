import pygame
from pygame import (K_w,
                    K_s,
                    K_a,
                    K_d,
                    K_ESCAPE,
                    KEYDOWN,
                    QUIT, )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((0, 0, 255))
        self.surf_location = ((SCREEN_WIDTH - 100) / 2, (SCREEN_LENGTH - 100) / 2)
        self.rect = self.surf.get_rect()

    def update_position(self, keys):

        if keys[K_w]:
            self.rect.move_ip(0, -1)
        if keys[K_s]:
            self.rect.move_ip(0, 1)
        if keys[K_a]:
            self.rect.move_ip(-1, 0)
        if keys[K_d]:
            self.rect.move_ip(1, 0)

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_LENGTH:
            self.rect.bottom = SCREEN_LENGTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


pygame.init()

SCREEN_WIDTH = 500
SCREEN_LENGTH = 650
screen = pygame.display.set_mode([500, 650])

player = Player()

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()
    player.update_position(pressed_keys)

    screen.fill((255, 255, 255))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

pygame.quit()
