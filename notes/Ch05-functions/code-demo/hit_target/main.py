# 1. divide the problem into small tasks
# 2. implement one task and test/debug till it works correctly
# 3. add more only if the current implementation works

import turtle

from setup_window import setup_window
from draw_target import draw_target_square
from get_inputs import get_user_inputs
from launch import launch_turtle
from check_hit import check_print

def main():
    setup_window()
    draw_target_square()

    hit = False
    while not hit:
        angle, distance = get_user_inputs()
        launch_turtle(angle, distance)
        hit = check_print()

    # keep the window open
    turtle.done()

if __name__ == '__main__':
    main()