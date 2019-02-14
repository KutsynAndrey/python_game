

def low_skill(enemy, ally):
    for bullet in ally.bullets:
        if bullet.x >= enemy.x - bullet.width and bullet.x+bullet.width <= enemy.x + enemy.width + bullet.width:
            if enemy.x + enemy.width // 2 > bullet.x + bullet.width // 2:
                enemy.move_right()
            else:
                enemy.move_left()

