
import pygame
from pygame import (
                    K_ESCAPE,
                    KEYDOWN,
                    QUIT,
                    MOUSEBUTTONDOWN)
from entities import Player, Enemy
from ui import UI

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

game_state = True




def main():
    global game_state

    clock = pygame.time.Clock()

    # Initialisation
    pygame.init()
    pygame.mixer.init()

    # Add Enemy Event
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    # Instantiate Player
    player = Player(SCREEN_WIDTH, SCREEN_LENGTH)

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
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_LENGTH, ENEMY_SPEED)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)


            elif event.type == MOUSEBUTTONDOWN:
                x, y = SCREEN_WIDTH / 2, SCREEN_LENGTH / 2
                mouse = pygame.mouse.get_pos()
                button_range = ((x, x + 86), (y, y + 31))

                if button_range[0][0] <= mouse[0] <= button_range[0][1] and button_range[1][0] <= mouse[1] <= \
                        button_range[1][1]:
                    print("hello")

        # Fill Background
        screen.fill(BG_COLOR)

        # Update Sprites
        pressed_keys = pygame.key.get_pressed()
        player.update_position(pressed_keys, PLAYER_SPEED)

        for enemy in enemies:
            enemy.update()

        # Draw Sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.death_sound.play(loops=0)
            player.kill()
            game_state = False

        if game_state is False:
            ui.restart_button(SCREEN_WIDTH/2, SCREEN_LENGTH/2, 20, COLOR_BLACK, screen)

        # Update Display
        pygame.display.flip()

        # Adjust Frustrate
        clock.tick(120)
        print(game_state)

    pygame.quit()


if __name__ == "__main__":
    main()
