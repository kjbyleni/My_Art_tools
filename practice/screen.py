import pygame


class Screen:

    def __init__(self, display: pygame.display):
        self.default_size = (1500, 1000)
        self.offset = 40
        self.full_screen = (display.Info().current_w, display.Info().current_h)
        self.display = display.set_mode(self.full_screen, pygame.FULLSCREEN)
        pygame.display.set_caption("Image practice")

    def get_active_size(self):
        if self.display.get_flags() & pygame.FULLSCREEN:
            # full screen mode return full screen
            return self.full_screen
        else:
            return self.default_size

    def toggle_full_screen(self, event):
        if event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if self.display.get_flags() & pygame.FULLSCREEN:
                self.display = pygame.display.set_mode(self.default_size)
            else:
                self.display = pygame.display.set_mode(self.full_screen, pygame.FULLSCREEN)


class Time:
    MINUTES = 1000 * 60

    def __init__(self, time_between_images):
        self.time = pygame.time
        self.old_ticks = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.time_between_images = time_between_images * Time.MINUTES

    def get_ticks(self):
        return self.time.get_ticks()

    def update_ticks(self):
        self.old_ticks = self.get_ticks()
        return self.old_ticks
