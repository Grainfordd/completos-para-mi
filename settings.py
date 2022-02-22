from pygame import image, transform 

class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (255, 255, 255)

        self.scale_factor = (1/1.5)
        self.bg_image = image.load('images/fondo.jpg')
        self.size = self.bg_image.get_width() * self.scale_factor, self.bg_image.get_height() * self.scale_factor
        self.bg_image = transform.scale(self.bg_image, self.size)

        # Kratos settings
        self.kratos_speed = 3
        self.lifes_limit = 2

        # Ball settings
        self.ball_speed = 3

        # Volume
        self.musica = 'music/07 - The End Begins.mp3'
        self.volume = 0.1

        

