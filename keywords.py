
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

