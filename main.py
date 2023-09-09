import pygame
from pygame import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN)
from entities import Player, Enemy
from ui import UI

game_state = True
running = True


class Main:
    def __init__(self, screen_width, screen_length, enemy_speed, player_speed, bg_color, color_black):
        # Configure Screen
        self.screen_width = screen_width
        self.screen_length = screen_length

        # Colors
        self.bg_color = bg_color
        self.color_black = color_black

        # Speed
        self.enemy_speed = enemy_speed
        self.player_speed = player_speed

        # Game State
        self.running = True
        self.game_state = True

        self.clock = pygame.time.Clock()

        pygame.init()

        # Add Enemy Event
        self.add_enemy = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_enemy, 250)

        # Instantiate Player and UI
        self.player = Player(self.screen_length, self.screen_width)
        self.ui = UI

        # Make Sprite Groups
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.run_game_loop()

    def run_event_manager(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

            elif event.type == self.add_enemy:
                new_enemy = Enemy(self.screen_width, self.screen_length, self.enemy_speed)
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)

            elif event.type == MOUSEBUTTONDOWN and game_state is False:
                x, y = self.screen_width / 2, self.screen_length / 2
                mouse = pygame.mouse.get_pos()
                button_range = ((x, x + 86), (y, y + 31))

                if button_range[0][0] <= mouse[0] <= button_range[0][1] and button_range[1][0] <= mouse[1] <= \
                        button_range[1][1]:
                    print("hello")

    def draw_sprites(self):
        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.death_sound.play(loops=0)
            self.player.kill()
            self.game_state = False

        if self.game_state is False:
            self.ui.restart_button(SCREEN_WIDTH / 2, SCREEN_LENGTH / 2, 20, self.color_black, screen)

    def run_game_loop(self):
        while self.running:

            self.run_event_manager()
            # Fill Background
            screen.fill(self.bg_color)

            # Update Sprites
            pressed_keys = pygame.key.get_pressed()
            self.player.update_position(pressed_keys, PLAYER_SPEED)

            for enemy in self.enemies:
                enemy.update()

            # Draw Sprites
            self.draw_sprites()

            # Update Display
            pygame.display.flip()
            print(self.game_state)
            # Adjust Frustrate
            self.clock.tick(120)



# Constants
SCREEN_WIDTH = 500
SCREEN_LENGTH = 650
BG_COLOR = (255, 255, 255)
ENEMY_COLOR = (255, 0, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 2
COLOR_BLACK = (0, 0, 0)

screen = pygame.display.set_mode([500, 650])

main = Main(SCREEN_WIDTH, SCREEN_LENGTH, ENEMY_SPEED, PLAYER_SPEED, BG_COLOR, COLOR_BLACK)