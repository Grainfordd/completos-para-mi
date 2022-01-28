import pygame
import random

class Ball:

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.scale_factor = 0.2
        self.image = pygame.image.load('images/ball.png')
        self.size = self.image.get_width() * self.scale_factor, self.image.get_height() * self.scale_factor
        self.image = pygame.transform.scale(self.image, (self.size))
        self.rect = self.image.get_rect()

        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery

        self.rect.top = self.screen_rect.top
        self.rect.centerx = self.screen_rect.centerx

    def update(self):
        self.rect.y += self.settings.ball_speed

        # if self.rect.bottom >= self.screen_rect.bottom:
        #     self.rect.top = self.screen_rect.top
        #     self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)


    def reset(self):
        self.rect.top = self.screen_rect.top
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)

        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
