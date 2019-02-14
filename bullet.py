from pygame import draw


class Bullet:

    def __init__(self, screen, **kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.speed = kwargs['speed']
        self.color = kwargs['color']
        self.screen = screen
        self.x = kwargs['coordinates'][0]
        self.y = kwargs['coordinates'][1]

    def create_bullet(self):
        draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        self.y -= self.speed
