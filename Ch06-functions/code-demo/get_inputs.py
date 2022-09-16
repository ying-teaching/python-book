import math
from setup_window import SCREEN_HEIGHT, SCREEN_WIDTH

MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT ** 2 + SCREEN_HEIGHT ** 2) / 2)

def get_user_inputs():
    angle = int(input("Enter the projectile's angle 0-360: "))
    distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}): '))
    return angle, distance