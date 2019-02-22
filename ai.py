
def low_skill(enemy, ally, last_shot, current_time):
    for bullet in ally.bullets:
        if bullet.x >= enemy.x - bullet.width and bullet.x+bullet.width <= enemy.x + enemy.width + bullet.width:
            if enemy.x + enemy.width // 2 > bullet.x + bullet.width // 2:
                enemy.move_right()
            else:
                enemy.move_left()

    if enemy.x > ally.x + ally.width:
            enemy.move_left()
    if enemy.x + enemy.width < ally.x:
            enemy.move_right()
    if enemy.x + enemy.width//2 < ally.x + ally.width and enemy.x +enemy.width//2 > ally.x:
        if current_time-last_shot >= enemy.fire_rate:
            enemy.add_bullet()

