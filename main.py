import pygame
import keywords as kw
import sys
from button import Button, collision_rect, window_resize
import units
import time
import ai

pygame.init()

sc = pygame.display.set_mode()
w, h = pygame.display.get_surface().get_size()
sk = (w, h)
kw.screen_size = sk
kw.last_ss = sk


def main_screen(screen):

    unit = units.units_pack[sk]['ally']["default_unit"]
    unit.screen = screen
    unit.x = w // 2 - unit.width // 2
    unit.y = h - h // 5
    last_shot = time.clock()
    bw = kw.settins_pack[sk]['button']['width']
    bh = kw.settins_pack[sk]['button']['height']

    start_ai = Button(screen,
                      width=bw,
                      height=bh,
                      text="START AI",
                      coordinates=(w // 4 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                      font_size=kw.settins_pack[sk]['button']['font_size'],
                      text_color=kw.colors["green"],
                      background_color=kw.colors["white"]
                      )

    game_settings = Button(screen,
                           width=bw,
                           height=bh,
                           text="SETTINGS",
                           coordinates=(w // 2 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                           font_size=kw.settins_pack[sk]['button']['font_size'],
                           text_color=kw.colors["green"],
                           background_color=kw.colors["white"]
                           )

    exit_b = Button(screen,
                    width=bw,
                    height=bh,
                    text="EXIT",
                    coordinates=(w - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                    font_size=kw.settins_pack[sk]['button']['font_size'],
                    text_color=kw.colors["green"],
                    background_color=kw.colors["white"]
                    )

    start_local = Button(screen,
                         width=bw,
                         height=bh,
                         text="MULTIPLAY",
                         coordinates=(w // 4 * 3 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                         font_size=kw.settins_pack[sk]['button']['font_size'],
                         text_color=kw.colors["green"],
                         background_color=kw.colors["white"]
                         )

    while 1:
        screen.fill(kw.colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            unit.move_left()
        if keys[pygame.K_RIGHT]:
            unit.move_right()
        if keys[pygame.K_UP]:
            current_shot = time.clock()
            if current_shot - last_shot >= unit.fire_rate:
                unit.add_bulled()
                last_shot = current_shot
        if keys[pygame.K_SPACE] and unit.laser is None:
            unit.create_laser()

        for bullet in unit.bullets:
                bullet.create_bullet()
                bullet.move_up()
                if bullet.y < -1*50:
                    unit.bullets.remove(bullet)
                if collision_rect(bullet, exit_b):
                    sys.exit()
                if collision_rect(bullet, start_ai):
                    kw.run = "start_with_ai"
                    unit.bullets.clear()
                    return
                if collision_rect(bullet, game_settings):
                    unit.bullets.clear()
                    kw.run = "settings"
                    unit.bullets.clear()
                    return
                if collision_rect(bullet, start_local):
                    kw.run = "start_local"
                    unit.bullets.clear()
                    return

        if unit.laser is not None:
            unit.laser.shot()
            if unit.laser.width <= 0:
                unit.laser = None

        game_settings.create_button()
        exit_b.create_button()
        start_local.create_button()
        start_ai.create_button()

        unit.check_border()
        unit.create_plane()
        pygame.display.update()


def settings(screen):
    unit = units.units_pack[sk]['ally']["default_unit"]
    unit.screen = screen
    unit.x = w // 2 - unit.width // 2
    unit.y = h - h // 5
    last_shot = time.clock()
    bw = kw.settins_pack[sk]['button']['width']
    bh = kw.settins_pack[sk]['button']['height']

    sound = Button(screen,
                   width=bw,
                   height=bh,
                   text="SOUND",
                   coordinates=(w // 4 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                   font_size=kw.settins_pack[sk]['button']['font_size'],
                   text_color=kw.colors["green"],
                   background_color=kw.colors["white"]
                   )

    display_size = Button(screen,
                          width=bw,
                          height=bh,
                          text="DISPLAY",
                          coordinates=(w // 2 - bw - ((w // 4 - bh) // 2), h // 2 - 35),
                          font_size=kw.settins_pack[sk]['button']['font_size'],
                          text_color=kw.colors["green"],
                          background_color=kw.colors["white"]
                          )

    back = Button(screen,
                  width=bw,
                  height=bh,
                  text="BACK",
                  coordinates=(w - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                  font_size=kw.settins_pack[sk]['button']['font_size'],
                  text_color=kw.colors["green"],
                  background_color=kw.colors["white"]
                  )

    FreeSpace = Button(screen,
                       width=bw,
                       height=bh,
                       text="",
                       coordinates=(w // 4 * 3 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                       font_size=kw.settins_pack[sk]['button']['font_size'],
                       text_color=kw.colors["green"],
                       background_color=kw.colors["white"]
                       )

    while 1:
        screen.fill(kw.colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            unit.move_left()
        if keys[pygame.K_RIGHT]:
            unit.move_right()
        if keys[pygame.K_UP]:
            current_shot = time.clock()
            if current_shot - last_shot >= unit.fire_rate:
                unit.add_bulled()
                last_shot = current_shot
        if keys[pygame.K_SPACE] and unit.laser is None:
            unit.create_laser()

        for bullet in unit.bullets:
            bullet.create_bullet()
            bullet.move_up()
            if bullet.y < -1 * 50:
                unit.bullets.remove(bullet)
            if collision_rect(bullet, back):
                unit.bullets.clear()
                kw.run = "main"
                return
            if collision_rect(bullet, sound):
                unit.bullets.clear()
            if collision_rect(bullet, display_size):
                unit.bullets.clear()
                kw.run = "display"
                return
            if collision_rect(bullet, FreeSpace):
                unit.bullets.clear()
                return

        if unit.laser is not None:
            unit.laser.shot()
            if unit.laser.width <= 0:
                unit.laser = None

        display_size.create_button()
        back.create_button()
        sound.create_button()
        FreeSpace.create_button()

        unit.check_border()
        unit.create_plane()
        pygame.display.update()


def display(screen):
    unit = units.units_pack[sk]['ally']["default_unit"]
    unit.screen = screen
    unit.x = w // 2 - unit.width // 2
    unit.y = h - h // 5
    last_shot = time.clock()
    bw = kw.settins_pack[sk]['button']['width']
    bh = kw.settins_pack[sk]['button']['height']

    full_hd = Button(screen,
                     width=bw,
                     height=bh,
                     text="1920x1080",
                     coordinates=(w // 4 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                     font_size=kw.settins_pack[sk]['button']['font_size'],
                     text_color=kw.colors["green"],
                     background_color=kw.colors["white"]
                     )

    WXGA = Button(screen,
                  width=bw,
                  height=bh,
                  text="1366x768",
                  coordinates=(w // 2 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                  font_size=kw.settins_pack[sk]['button']['font_size'],
                  text_color=kw.colors["green"],
                  background_color=kw.colors["white"]
                  )

    back = Button(screen,
                  width=bw,
                  height=bh,
                  text="BACK",
                  coordinates=(w - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                  font_size=kw.settins_pack[sk]['button']['font_size'],
                  text_color=kw.colors["green"],
                  background_color=kw.colors["white"]
                  )

    fullscreen = Button(screen,
                        width=bw,
                        height=bh,
                        text="FullScreen",
                        coordinates=(w // 4 * 3 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                        font_size=kw.settins_pack[sk]['button']['font_size'],
                        text_color=kw.colors["green"],
                        background_color=kw.colors["white"]
                        )

    while 1:
        screen.fill(kw.colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            unit.move_left()
        if keys[pygame.K_RIGHT]:
            unit.move_right()
        if keys[pygame.K_UP]:
            current_shot = time.clock()
            if current_shot - last_shot >= unit.fire_rate:
                unit.add_bulled()
                last_shot = current_shot
        if keys[pygame.K_SPACE] and unit.laser is None:
            unit.create_laser()

        for bullet in unit.bullets:
            bullet.create_bullet()
            bullet.move_up()
            if bullet.y < -1 * 50:
                unit.bullets.remove(bullet)
            if collision_rect(bullet, back):
                unit.bullets.clear()
                kw.run = "settings"
                return
            if collision_rect(bullet, full_hd):
                unit.bullets.clear()
                kw.screen_size = (1920, 1080)
                return
            if collision_rect(bullet, WXGA):
                unit.bullets.clear()
                kw.screen_size = (1366, 768)
                return
            if collision_rect(bullet, fullscreen):
                unit.bullets.clear()
                return

        if unit.laser is not None:
            unit.laser.shot()
            if unit.laser.width <= 0:
                unit.laser = None

        full_hd.create_button()
        back.create_button()
        WXGA.create_button()
        fullscreen.create_button()

        unit.check_border()
        unit.create_plane()
        pygame.display.update()


def start_with_ai(screen):
    unit = units.units_pack[sk]['ally']["default_unit"]
    unit.screen = screen
    unit.x = w // 2 - unit.width // 2
    unit.y = h - h // 5
    last_shot = time.clock()
    bw = kw.settins_pack[sk]['button']['width']
    bh = kw.settins_pack[sk]['button']['height']

    low_skill = Button(screen,
                       width=bw,
                       height=bh,
                       text="LOW",
                       coordinates=(w // 4 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                       font_size=kw.settins_pack[sk]['button']['font_size'],
                       text_color=kw.colors["green"],
                       background_color=kw.colors["white"]
                       )

    medium_skill = Button(screen,
                          width=bw,
                          height=bh,
                          text="MEDIUM",
                          coordinates=(w // 2 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                          font_size=kw.settins_pack[sk]['button']['font_size'],
                          text_color=kw.colors["green"],
                          background_color=kw.colors["white"]
                          )

    back = Button(screen,
                  width=bw,
                  height=bh,
                  text="BACK",
                  coordinates=(w - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                  font_size=kw.settins_pack[sk]['button']['font_size'],
                  text_color=kw.colors["green"],
                  background_color=kw.colors["white"]
                  )

    hard_skill = Button(screen,
                        width=bw,
                        height=bh,
                        text="HARD",
                        coordinates=(w // 4 * 3 - bw - ((w // 4 - bw) // 2), h // 2 - 35),
                        font_size=kw.settins_pack[sk]['button']['font_size'],
                        text_color=kw.colors["green"],
                        background_color=kw.colors["white"]
                        )

    while 1:
        screen.fill(kw.colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            unit.move_left()
        if keys[pygame.K_RIGHT]:
            unit.move_right()
        if keys[pygame.K_UP]:
            current_shot = time.clock()
            if current_shot - last_shot >= unit.fire_rate:
                unit.add_bulled()
                last_shot = current_shot
        if keys[pygame.K_SPACE] and unit.laser is None:
            unit.create_laser()

        for bullet in unit.bullets:
            bullet.create_bullet()
            bullet.move_up()
            if bullet.y < -1 * 50:
                unit.bullets.remove(bullet)
            if collision_rect(bullet, back):
                unit.bullets.clear()
                kw.run = "main"
                return
            if collision_rect(bullet, medium_skill):
                unit.bullets.clear()
                return
            if collision_rect(bullet, hard_skill):
                unit.bullets.clear()
                return
            if collision_rect(bullet, low_skill):
                kw.run = 'fight'
                kw.difficult = 'low'
                unit.bullets.clear()
                return

        if unit.laser is not None:
            unit.laser.shot()
            if unit.laser.width <= 0:
                unit.laser = None

        hard_skill.create_button()
        back.create_button()
        low_skill.create_button()
        medium_skill.create_button()

        unit.check_border()
        unit.create_plane()
        pygame.display.update()


def fight_with_ai(screen):
    unit = units.units_pack[sk]['ally']["default_unit"]
    unit.screen = screen
    unit.x = w // 2 - unit.width // 2
    unit.y = h - h // 5
    last_shot = time.clock()

    enemy_unit = units.units_pack[sk]['enemy']["default_unit"]
    enemy_unit.screen = screen
    enemy_unit.x = w // 2 - unit.width // 2
    enemy_unit.y = h // 5
    enemy_last_shot = time.clock()

    while 1:
        screen.fill(kw.colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            unit.move_left()
        if keys[pygame.K_RIGHT]:
            unit.move_right()
        if keys[pygame.K_UP]:
            current_shot = time.clock()
            if current_shot - last_shot >= unit.fire_rate:
                unit.add_bulled()
                last_shot = current_shot
        if keys[pygame.K_SPACE] and unit.laser is None:
            unit.create_laser()

        for bullet in unit.bullets:
            bullet.create_bullet()
            bullet.move_up()
            if bullet.y < -1 * 50:
                unit.bullets.remove(bullet)
            elif collision_rect(enemy_unit, bullet):
                enemy_unit.health -= 5
                unit.bullets.remove(bullet)

        if unit.laser is not None:
            unit.laser.shot()
            if unit.laser.width <= 0:
                unit.laser = None

        if kw.difficult == 'low':
            ai.low_skill(enemy_unit, unit)

        enemy_unit.health_bar()
        unit.health_bar()
        unit.check_border()
        unit.create_plane()
        enemy_unit.create_plane()
        enemy_unit.check_border()
        pygame.display.update()


while 1:
    if kw.run == "main":
        main_screen(sc)

    elif kw.run == "settings":
        settings(sc)
    elif kw.run == "display":
        display(sc)
        if kw.last_ss != kw.screen_size:
            sc = window_resize(kw.screen_size)
            kw.last_ss = kw.screen_size
            w, h = pygame.display.get_surface().get_size()
            sk = (w, h)
            display(sc)
    elif kw.run == 'start_with_ai':
        start_with_ai(sc)
    elif kw.run == 'fight':
        fight_with_ai(sc)


