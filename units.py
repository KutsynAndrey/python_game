from aircraft import Plane
from keywords import colors

units_pack = {
    (1920, 1080): {
        'ally':
        {
            "default_unit": Plane(None,
                                  width=100,
                                  height=100,
                                  color=colors['white'],
                                  coordinates=(None, None),
                                  form='rect',
                                  speed=10,
                                  bullet_width=10,
                                  bullet_height=20,
                                  bullet_color=colors["pink"],
                                  bullet_speed=20,
                                  sprite=None,
                                  laser_color=colors["white"],
                                  laser_width=35,
                                  fire_rate=0.4,
                                  side="ally"
                                  )
        },
        'enemy':
        {
            "default_unit": Plane(None,
                                  width=100,
                                  height=100,
                                  color=colors['white'],
                                  coordinates=(None, None),
                                  form='rect',
                                  speed=10,
                                  bullet_width=10,
                                  bullet_height=20,
                                  bullet_color=colors["pink"],
                                  bullet_speed=10,
                                  sprite=None,
                                  laser_color=colors["white"],
                                  laser_width=35,
                                  fire_rate=0.4,
                                  side="enemy"
                                  )
        }
    },
    (1366, 768): {
        "ally":
        {
            "default_unit": Plane(None,
                                  width=75,
                                  height=75,
                                  color=colors['white'],
                                  coordinates=(None, None),
                                  form='rect',
                                  speed=7,
                                  bullet_width=7,
                                  bullet_height=15,
                                  bullet_color=colors["pink"],
                                  bullet_speed=7,
                                  sprite=None,
                                  laser_color=colors["white"],
                                  laser_width=25,
                                  fire_rate=0.4,
                                  side="ally"
                                  )
        },
        "enemy":
        {
            "default_unit": Plane(None,
                                  width=75,
                                  height=75,
                                  color=colors['white'],
                                  coordinates=(None, None),
                                  form='rect',
                                  speed=7,
                                  bullet_width=7,
                                  bullet_height=15,
                                  bullet_color=colors["pink"],
                                  bullet_speed=7,
                                  sprite=None,
                                  laser_color=colors["white"],
                                  laser_width=25,
                                  fire_rate=0.4,
                                  side="enemy"
                                  )
        }
    }
}


