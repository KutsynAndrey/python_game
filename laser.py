from pygame import draw


class Laser:
    def __init__(self, screen, **kwargs):
        self.color = kwargs['color']
        self.screen = screen
        self.width = kwargs['width']
        self.x = kwargs['coordinates'][0]
        self.y = kwargs['coordinates'][1]
        self.length = kwargs['length']

    def shot(self):
        draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y - self.length), self.width)
        self.width -= 1
