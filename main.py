from pygame import display, event, QUIT, KEYDOWN, init, mixer
from pygame.font import SysFont
from gameloop import GameLoop
from entities import Player


class MainMenu:
    def __init__(self):
        init()
        # Screen
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_LENGTH])
        display.set_caption("Flappy Shapes")
        self.main_menu_running = True
        self.player = Player(SCREEN_WIDTH, SCREEN_LENGTH, (100, 100))

        # Background Music
        bg_music = mixer.Sound("Audio/background_music.mp3")
        bg_music.set_volume(0.3)
        bg_music.play()

        while self.main_menu_running:

            for this_event in event.get():
                if this_event.type == QUIT:
                    self.main_menu_running = False
                if this_event.type == KEYDOWN:
                    self.main_menu_running = False
                    game_loop = GameLoop(self.screen, ENEMY_SPEED, PLAYER_SPEED, WHITE_COLOR, COLOR_BLACK)
                    if not game_loop.running:
                        self.main_menu_running = True

            self.screen.fill((255, 255, 255))
            self.display_text()
            self.display_player()

            display.flip()

    def display_text(self):
        title_font = SysFont("arial", 30)
        subtext_font = SysFont("comicsansms", 20)
        title = title_font.render("Flappy Shapes", True, (0, 0, 0))
        self.screen.blit(title, (SCREEN_WIDTH / 2 - 90, SCREEN_LENGTH / 12))

        subtext = subtext_font.render("Press Any Key to Play!", True, (2, 145, 150))
        self.screen.blit(subtext, (SCREEN_WIDTH / 2, SCREEN_LENGTH / 7))

    def display_player(self):
        self.screen.blit(self.player.surf, self.player.rect)


# Constants
SCREEN_WIDTH = 500
SCREEN_LENGTH = 650
WHITE_COLOR = (255, 255, 255)
ENEMY_COLOR = (255, 0, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 2
COLOR_BLACK = (0, 0, 0)

MainMenu()
