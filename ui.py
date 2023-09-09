from pygame.font import Font


class UI:
    @staticmethod
    def restart_button(x, y, size, text_color, screen):
        font = Font("Fonts/Inter-Medium.ttf", size)
        text = font.render("Restart", True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
