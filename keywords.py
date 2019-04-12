from pygame import image

EXIT = image.load('game/glob_img/EXIT.jpg')
SETTINGS = image.load('game/glob_img/SETTINGS.jpg')
BACK = image.load('game/glob_img/BACK.jpg')
CLIENT = image.load('game/glob_img/CLIENT.jpg')
CREATE = image.load('game/glob_img/CREATE.jpg')
DISPLAY = image.load('game/glob_img/DISPLAY.jpg')
FREE_SPACE = image.load('game/glob_img/FREE_SPACE.jpg')
FULL_SCREEN = image.load('game/glob_img/FULL_SCREEN.jpg')
HARD_AI = image.load('game/glob_img/HARD_AI.jpg')
LOW_AI = image.load('game/glob_img/LOW_AI.jpg')
MEDIUM_AI = image.load('game/glob_img/MEDIUM_AI.jpg')
MULTIPLAY = image.load('game/glob_img/MULTIPLAY.jpg')
SERVER = image.load('game/glob_img/SERVER.jpg')
SOUND = image.load('game/glob_img/SOUND.jpg')
START_AI = image.load('game/glob_img/START_AI.jpg')

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "blue": (0, 204, 255),
    "brown": (102, 0, 0),
    "purple": (102, 0, 102),
    "pink": (255, 51, 153)
}


settins_pack = {
    (1920, 1080): {
        "button": {
            "width": 250,
            "height": 90,
            "font_size": 65
        },
        "width": 1920,
        "height": 1080,
        "units": {
            "width": 100,
            "height": 100,
        },
        'input_field': {
            "width": 400,
            "height": 150,
            "font_size": 65
        }
    },
    (1366, 768): {
        "button": {
            "width": 200,
            "height": 70,
            "font_size": 50
        },
        "width": 1366,
        "height": 768,
        "units": {
            "width": 75,
            "height": 75,
        },
        'input_field': {
            "width": 330,
            "height": 100,
            "font_size": 50
        }
    }
}

run = "main"
sound = 'on'
difficult = None
screen_size = None
last_ss = None
pause = 0
ip = None
port = None
side = None


def create_current_settings(window_size):
    pack = {
        window_size: {
            "button": {
                "width": window_size[0] // 7,
                "height": window_size[1] // 10,
                "font_size": 50
            },
            "width": 1366,
            "height": 768,
            "units": {
                "width": 75,
                "height": 75,
            }
        }
    }

