import pygame

class Kratos:

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.scale_factor = 0.7
        self.image = pygame.image.load('images/kratos.png')
        self.size = self.image.get_width() * self.scale_factor, self.image.get_height() * self.scale_factor
        self.image = pygame.transform.scale(self.image, (self.size))
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.direction = 1    # 1 for right, -1 for left

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.kratos_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.kratos_speed

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
