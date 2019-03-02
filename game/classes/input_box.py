from pygame import draw, key, font, Rect
from pygame import MOUSEBUTTONDOWN, KEYDOWN, K_BACKSPACE, K_RETURN
from keywords import colors


class InputBox:

    def __init__(self, screen, **kwargs):
        self.screen = screen
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.color = kwargs['color']
        self.border_width = kwargs['border_width']
        self.active_color = kwargs['active_color']
        self.no_active_color = kwargs['no_active_color']
        self.x = kwargs['coordinates'][0]
        self.y = kwargs['coordinates'][1]
        self.font_size = kwargs['font_size']
        self.text = ''
        self.text_color = kwargs['text_color']
        self.active = False
        self.Rect = Rect(self.x, self.y, self.width, self.height)
        self.border_color = self.no_active_color
        self.text_surface = None
        self.field_name = kwargs['field_name']
        self.enter = False

    def render(self):
        font2 = font.Font(None, self.font_size)
        font1 = font.Font(None, self.font_size)
        text = font1.render(self.text, 0, self.text_color)
        text2 = font2.render(self.field_name, 0, self.border_color)
        self.text_surface = text
        draw.rect(self.screen, colors['black'], (self.x, self.y, self.width, self.height))
        self.screen.blit(text, (self.x + self.border_width, self.y + self.border_width))
        self.screen.blit(text2, (self.x + text2.get_width() // 2, self.y - text2.get_height()))
        draw.rect(self.screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)

    def check_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.Rect.collidepoint(event.pos[0], event.pos[1]):
                if self.active:
                    self.active = False
                    self.border_color = self.no_active_color
                else:
                    self.active = True
                    self.border_color = self.active_color
            else:
                self.active = False
                self.border_color = self.no_active_color
        elif event.type == KEYDOWN:
            if self.active:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.text_surface.get_width() < self.width - 30:
                        self.text += event.unicode
                if event.key == K_RETURN:
                    self.enter = True









