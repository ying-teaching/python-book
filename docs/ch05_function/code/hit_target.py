# Hit the Target Game
import math
import random
import turtle

# Named constants
SCREEN_WIDTH = 600  # Screen width
SCREEN_HEIGHT = 600  # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT**2 + SCREEN_HEIGHT**2) / 2)

TARGET_LOWER_LEFT_X = 100  # Target's lower-left X
TARGET_LOWER_LEFT_Y = 100  # Target's lower-left Y
TARGET_WIDTH = 50  # Width of the target

SPEED = 0  # Projectile's animation speed

EAST = 0  # Angle of east direction
NORTH = 90  # Angle of north direction
SOUTH = 270  # Angle of south direction
WEST = 180  # Angle of west direction


def initialize():
    # for repeatable experiments
    random.seed(2023)

    # Setup the window.
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def draw_target(turtle):
    turtle.hideturtle()
    turtle.speed(SPEED)
    turtle.up()
    turtle.goto(TARGET_LOWER_LEFT_X, TARGET_LOWER_LEFT_Y)
    turtle.down()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.up()


def launch_test(turtle):
    is_hit = False
    while not is_hit:
        # Center the turtle.
        turtle.home()
        turtle.showturtle()
        turtle.speed(SPEED)

        # Get the angle and force from the user.
        angle = random.randint(0, 90)
        distance = random.randint(0, MAX_DISTANCE + 1)

        # Set the heading.
        turtle.setheading(angle)

        # Launch the projectile.
        turtle.down()
        turtle.forward(distance)

        is_hit = check_hit(turtle)

        # show message
        if is_hit:
            print("Target hit!")
        else:
            print("You missed the targe.")


def check_hit(turtle):
    xcor = turtle.xcor()
    ycor = turtle.ycor()

    # Did it hit the target?
    is_in_x = (xcor >= TARGET_LOWER_LEFT_X) and (
        xcor <= (TARGET_LOWER_LEFT_X + TARGET_WIDTH)
    )
    is_in_y = (ycor >= TARGET_LOWER_LEFT_Y) and (
        ycor <= (TARGET_LOWER_LEFT_Y + TARGET_WIDTH)
    )
    is_hit = is_in_x and is_in_y
    return is_hit


def main():
    initialize()
    my_turtle = turtle.Turtle()
    draw_target(my_turtle)
    launch_test(my_turtle)

    my_turtle.screen.mainloop()


main()
