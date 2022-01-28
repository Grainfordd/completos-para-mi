from pygame import image, transform

class Background:

    def __init__(self):
        self.scale_factor = (1/1.5)
        self.image = image.load('images/fondo.jpg')
        size = self.image.get_width() * self.scale_factor, self.image.get_height() * self.scale_factor
        self.image = transform.scale(self.image, size)


