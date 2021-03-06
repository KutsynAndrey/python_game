from game.classes.bullet import Bullet
from game.classes.laser import Laser
from pygame import draw
from time import clock


class Plane:

    def __init__(self, screen, **kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.color = kwargs['color']
        self.x = kwargs['coordinates'][0]
        self.y = kwargs['coordinates'][1]
        self.screen = screen
        self.form = kwargs['form']
        self.speed = kwargs['speed']
        self.bullet_speed = kwargs['bullet_speed']
        self.sprite = kwargs['sprite']
        self.bullet_color = kwargs['bullet_color']
        self.bullet_width = kwargs['bullet_width']
        self.bullet_height = kwargs['bullet_height']
        self.bullets = []
        self.laser = None
        self.fire_rate = kwargs['fire_rate']
        self.laser_fire_rate = kwargs['laser_fire_rate']
        self.laser_color = kwargs['laser_color']
        self.laser_width = kwargs['laser_width']
        self.health = 100
        self.side = kwargs['side']
        self.last_bullet = clock() - self.fire_rate
        self.last_laser = clock() - self.laser_fire_rate

    def create_laser(self):
        t = clock()
        if t - self.last_laser > self.laser_fire_rate:
            self.last_laser = t
            laser = Laser(self.screen,
                          color=self.laser_color,
                          width=self.laser_width,
                          coordinates=(self.x + self.width // 2 - self.laser_width // 2, self.y + 10),
                          length=self.screen.get_height()
                          )
            self.laser = laser

    def create_plane(self):
        if self.sprite is None:
            if self.form == 'rect':
                draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            self.screen.blit(self.sprite, (self.x, self.y))

    def add_bullet(self):
        t = clock()
        if t - self.last_bullet > self.fire_rate:
            self.last_bullet = t
            if self.side == 'enemy':
                bullet = Bullet(self.screen,
                                width=self.bullet_width,
                                height=self.bullet_height,
                                speed=self.bullet_speed,
                                color=self.bullet_color,
                                coordinates=(self.x + self.width // 2, self.y + self.height)
                                )
            else:
                bullet = Bullet(self.screen,
                                width=self.bullet_width,
                                height=self.bullet_height,
                                speed=self.bullet_speed,
                                color=self.bullet_color,
                                coordinates=(self.x + self.width // 2, self.y)
                                )
            self.bullets.append(bullet)

    def move_right(self):
        self.x += self.speed

    def check_border(self):
        w = self.screen.get_width()
        h = self.screen.get_height()
        if self.x < -1*self.width:
            self.x = w
        if self.x > w:
            self.x = -1*self.width

    def move_left(self):
        self.x -= self.speed

    def health_bar(self):
        if self.health > 0:
            height = self.height // 7
            width = int(self.width * (self.health / 100))
            color = (255, 0, 0)
            if self.side == 'ally':
                draw.rect(self.screen, color, (self.x, self.y - self.height//10 - height, width, height))
            else:
                draw.rect(self.screen, color, (self.x, self.y + self.height + self.height // 10, width, height))

    def pack(self):
        bullets_coords = []
        unit_coord = self.x
        unit_health = self.health
        for i in self.bullets:
            bullets_coords.append(i.x)

        return bullets_coords, unit_coord, unit_health

    def unpack(self, data):
        self.bullets.clear()
        for i in range(len(data[0])):
            bullet = Bullet(self.screen,
                            width=self.bullet_width,
                            height=self.bullet_height,
                            speed=self.bullet_speed,
                            color=self.bullet_color,
                            coordinates=(data[0][i], self.y + self.height)
                            )
            self.bullets.append(bullet)
        self.x = data[1]
        self.health = data[2]