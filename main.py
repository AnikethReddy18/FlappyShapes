import random
import pygame
from pygame import (K_w,
                    K_s,
                    K_a,
                    K_d,
                    K_ESCAPE,
                    KEYDOWN,
                    QUIT)

# Constants
SCREEN_WIDTH = 500
SCREEN_LENGTH = 650
BG_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 2
COLOR_BLACK = (0, 0, 0)

screen = pygame.display.set_mode([500, 650])


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.death_sound = pygame.mixer.Sound("Audio/player_death.mp3")
        image = pygame.image.load("Images/flappy_bird.png").convert_alpha()

        self.surf = pygame.transform.scale(image, (50, 50))

        self.rect = self.surf.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_LENGTH / 2)

    def update_position(self, keys):

        if keys[K_w]:
            self.rect.move_ip(0, -PLAYER_SPEED)
        if keys[K_s]:
            self.rect.move_ip(0, PLAYER_SPEED)
        if keys[K_a]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[K_d]:
            self.rect.move_ip(PLAYER_SPEED, 0)

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
        image = pygame.image.load("Images/rock.png").convert_alpha()
        self.surf = pygame.transform.scale(image, (30, 30))
        self.rect = self.surf.get_rect()
        enemy_position = (SCREEN_WIDTH, random.randint(10, SCREEN_LENGTH - 10))
        self.rect.center = enemy_position
        self.death_sound = pygame.mixer.Sound("Audio/player_death.mp3")

    def update(self):
        self.rect.x -= ENEMY_SPEED


class UI:
    @staticmethod
    def draw_button(x, y, size, text):
        font = pygame.font.Font("Fonts/Inter-Medium.ttf", size)
        text = font.render(text, True, COLOR_BLACK)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)


def main():
    clock = pygame.time.Clock()

    # Initialisation
    pygame.init()
    pygame.mixer.init()

    # Add Enemy Event
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    # Instantiate Player
    player = Player()

    # Instantiate UI
    ui = UI

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

            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Fill Background
        screen.fill(BG_COLOR)

        # Update Sprites
        pressed_keys = pygame.key.get_pressed()
        player.update_position(pressed_keys)

        for enemy in enemies:
            enemy.update()

        # Draw Sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.death_sound.play(loops=0)
            player.kill()
            running = False

        # Buttons
        ui.draw_button(SCREEN_WIDTH/2, 25, "Restart")

        # Update Display
        pygame.display.flip()



        # Adjust Frustrate
        clock.tick(120)

    pygame.quit()


if __name__ == "__main__":
    main()
