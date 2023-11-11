
import pygame
from pygame import QUIT
from entities import Player, Enemy


class GameLoop:
    def __init__(self, screen, enemy_speed, player_speed, bg_color, color_black):
        # Configure Screen
        self.screen = screen
        self.screen_width, self.screen_length = screen.get_size()
        # Colors
        self.bg_color = bg_color
        self.color_black = color_black

        # Speed
        self.enemy_speed = enemy_speed
        self.player_speed = player_speed

        # Game State
        self.running = True
        self.game_over = False
        self.exit_game = False

        self.clock = pygame.time.Clock()

        pygame.init()

        # Add Enemy Event
        self.add_enemy = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_enemy, 250)

        # Instantiate Player and UI
        self.player = Player(self.screen_width, self.screen_length)

        # Make Sprite Groups
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.in_score = pygame.time.get_ticks()
        self.run_game_loop()

    def run_event_manager(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.exit_game = True

            elif event.type == self.add_enemy:
                new_enemy = Enemy(self.screen_width, self.screen_length, self.enemy_speed)
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)

    def draw(self):
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)

    def run_game_loop(self):
        while self.running:

            self.run_event_manager()
            # Fill Background
            self.screen.fill(self.bg_color)

            # Update Sprites
            pressed_keys = pygame.key.get_pressed()
            self.player.update_position(pressed_keys, self.player_speed)

            for enemy in self.enemies:
                enemy.update()

            # Draw Sprites
            self.draw()

            # Replay Game if player dies
            self.check_death()

            # Display Score
            self.score_counter()

            # Update Display
            pygame.display.flip()

            # Adjust Framer
            self.clock.tick(120)

    def check_death(self):
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.death_sound.play(loops=0)
            self.running = False

    def score_counter(self):
        score = (pygame.time.get_ticks() - self.in_score) // 1000
        font = pygame.font.SysFont("arial", 20)
        score_render = font.render(str(score), True, (0, 0, 0))
        self.screen.blit(score_render, (50, 50))
