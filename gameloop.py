import pygame
from pygame import QUIT
from entities import Player, Enemy, Heart, MoveHeart


class GameLoop:
    def __init__(self, screen, enemy_speed, player_speed, bg_color, color_black):
        # Configure Screen
        self.score = 0
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

        # Hearts
        self.no_hearts = 3
        self.no_hearts_td = self.no_hearts
        self.prev_heart_pos = [20, 20]

        # Add Event
        self.add_enemy = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_enemy, 250)
        self.increase_ene_speed = pygame.USEREVENT + 2
        pygame.time.set_timer(self.increase_ene_speed, 15000)

        self.give_heart = pygame.USEREVENT + 3
        pygame.time.set_timer(self.give_heart, 7000)

        # Instantiate Player and UI
        self.player = Player(self.screen_width, self.screen_length)

        # Make Sprite Groups
        self.enemies = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.in_score = pygame.time.get_ticks()
        self.run_game_loop()

    def run_event_manager(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.exit_game = True

            if event.type == self.add_enemy:
                new_enemy = Enemy(self.screen_width, self.screen_length, self.enemy_speed)
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)

            if event.type == self.give_heart:
                heart = MoveHeart()
                self.hearts.add(heart)
                self.all_sprites.add(heart)

            if event.type == self.increase_ene_speed:
                self.enemy_speed += 1

    def draw(self):
        for _ in range(0, self.no_hearts_td):
            heart = Heart(self.prev_heart_pos[0], self.prev_heart_pos[1])
            self.all_sprites.add(heart)
            self.prev_heart_pos[0] += 35
            self.no_hearts_td -= 1

        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)

        for enemy in self.enemies:
            enemy.update()

        for heart in self.hearts:
            heart.update()

    def run_game_loop(self):
        while self.running:
            self.run_event_manager()

            # Fill Background
            self.screen.fill(self.bg_color)

            # Update Sprites
            pressed_keys = pygame.key.get_pressed()
            self.player.update_position(pressed_keys, self.player_speed)

            # Draw Sprites
            self.draw()

            # Check collision
            self.check_collision()

            # Display Score
            self.score_counter()

            # Update Display
            pygame.display.flip()

            # Adjust Framer
            self.clock.tick(120)

    def check_collision(self):
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.death_sound.play(loops=0)
            self.no_hearts = self.no_hearts - 1
            self.no_hearts_td = self.no_hearts

            self.start_again()

        if self.no_hearts == 0:
            self.running = False

        if pygame.sprite.spritecollideany(self.player, self.hearts):
            self.no_hearts += 1
            self.no_hearts_td += 1

            self.player.heart_capture_sound.play(loops=0)
            for heart in self.hearts:
                heart.kill()

    def score_counter(self):
        self.score = (pygame.time.get_ticks() - self.in_score) // 1000
        font = pygame.font.SysFont("arial", 20)
        score_render = font.render(str(self.score), True, (0, 0, 0))
        self.screen.blit(score_render, (50, 50))

    def start_again(self):
        for sprite in self.all_sprites:
            if sprite != self.player:
                sprite.kill()

        self.player.rect.center = (self.screen_width / 2, self.screen_length / 2)
        self.prev_heart_pos = [20, 20]
