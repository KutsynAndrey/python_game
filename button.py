from pygame import draw, display, font


class Button:

    def __init__(self, screen, **kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.text = kwargs['text']
        self.x = kwargs['coordinates'][0]
        self.y = kwargs['coordinates'][1]
        self.screen = screen
        self.font_size = kwargs['font_size']
        self.text_color = kwargs['text_color']
        self.background_color = kwargs['background_color']

    def write_text(self):
        font1 = font.Font(None, self.font_size)
        text = font1.render(self.text, 0, self.text_color)
        self.screen.blit(text, (self.x, self.y))

    def draw_background(self):
        draw.rect(self.screen, self.background_color, (self.x, self.y, self.width, self.height))

    def create_button(self):
        self.draw_background()
        self.write_text()


def collision_rect(object1, object2):
        tl1x = object1.x
        tl1y = object1.y
        tr1x = object1.x + object1.width
        tr1y = object1.y
        bl1x = object1.x
        bl1y = object1.y + object1.height
        br1x = object1.x + object1.width
        br1y = object1.y + object1.height

        tl2x = object2.x
        tl2y = object2.y
        tr2x = object2.x + object2.width
        tr2y = object2.y
        bl2x = object2.x
        bl2y = object2.y + object2.height
        br2x = object2.x + object2.width
        br2y = object2.y + object2.height

        if tl1x < br2x and tl1y < br2y and tl1x > bl2x and tl1y > tr2y:
            return True
        elif tr1x > bl2x and tr1x < br2x and tr1y < br2y and tr1y > tr2y:
            return True
        elif bl1x < tr2x and bl1x > tl2x and bl1y > tl2y and bl1y < bl2y:
            return True
        elif br1x > tl2x and br1x < tr2x and br1y > tl2y and br1y < bl2y:
            return True
        elif tl2x < br1x and tl2y < br1y and tl2x > bl1x and tl2y > tr1y:
            return True
        elif tr2x > bl1x and tr2x < br1x and tr2y < br1y and tr2y > tr1y:
            return True
        elif bl2x < tr1x and bl2x > tl1x and bl2y > tl1y and bl2y < bl1y:
            return True
        elif br2x > tl1x and br2x < tr1x and br2y > tl1y and br2y < bl1y:
            return True
        else:
            return False


def collision_line_rect(rect, line):
    pass


def window_resize(size):
    return display.set_mode(size)



