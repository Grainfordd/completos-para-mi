from kratos import Kratos
import pygame


class Vidas(Kratos):

    def __init__(self, settings, screen, stats):

        super().__init__(settings, screen)
        self.stats = stats

        self.scale_factor = 0.35
        self.image = pygame.image.load('images/kratos.png')
        self.size = self.image.get_width() * self.scale_factor, self.image.get_height() * self.scale_factor
        self.image = pygame.transform.scale(self.image, (self.size))
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()

        self.rect.left = self.screen_rect.left 
        self.rect.top = self.screen_rect.top


    def blitme(self):

        for vidas_restantes in range(self.stats.lifes_left + 1):
            self.screen.blit(self.image, (self.rect.left + vidas_restantes * self.width, self.rect.top))

