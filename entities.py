from pygame.sprite import Sprite
from pygame.mixer import Sound
from pygame.image import load
from pygame.transform import scale
from pygame import (K_w,
                    K_s,
                    K_a,
                    K_d)
import random


class Player(Sprite):
    def __init__(self, screen_width, screen_length, size=(50, 50)):
        super().__init__()

        self.screen_width = screen_width
        self.screen_length = screen_length

        self.death_sound = Sound("Audio/player_death.mp3")
        image = load("Images/flappy_bird.png").convert_alpha()

        self.surf = scale(image, size)

        self.rect = self.surf.get_rect()
        self.rect.center = (self.screen_width / 2, self.screen_length / 2)

    def update_position(self, keys, player_speed):

        if keys[K_w]:
            self.rect.move_ip(0, -player_speed)
        if keys[K_s]:
            self.rect.move_ip(0, player_speed)
        if keys[K_a]:
            self.rect.move_ip(-player_speed, 0)
        if keys[K_d]:
            self.rect.move_ip(player_speed, 0)

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_length:
            self.rect.bottom = self.screen_length
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width


class Enemy(Sprite):
    def __init__(self, screen_width, screen_length, speed):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.speed = speed

        image = load("Images/rock.png").convert_alpha()
        self.surf = scale(image, (30, 30))
        self.rect = self.surf.get_rect()
        enemy_position = (self.screen_width, random.randint(10, self.screen_length - 10))
        self.rect.center = enemy_position
        self.death_sound = Sound("Audio/player_death.mp3")

    def update(self):
        self.rect.x -= self.speed
