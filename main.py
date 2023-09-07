import random
import pygame
from pygame import (K_w,
                    K_s,
                    K_a,
                    K_d,
                    K_n,
                    K_ESCAPE,
                    KEYDOWN,
                    QUIT, )

# Constants
SCREEN_WIDTH = 500
SCREEN_LENGTH = 650
BG_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(PLAYER_COLOR)
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_LENGTH / 2)

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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill(ENEMY_COLOR)
        self.rect = self.surf.get_rect()
        enemy_position = (20, random.randint(10, SCREEN_LENGTH - 10))
        self.rect.center = enemy_position

    def update(self):
        self.rect.move_ip(1, 0)


def main():
    pygame.init()

    # Main Screen
    screen = pygame.display.set_mode([500, 650])

    player = Player()

    # Sprite Groups
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Game loop
    running = True
    while running:

        # Event Manager
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_n:
                    enemy = Enemy()

        # Fill Background
        screen.fill(BG_COLOR)

        # Update Positions
        pressed_keys = pygame.key.get_pressed()
        player.update_position(pressed_keys)

        # Draw Sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
