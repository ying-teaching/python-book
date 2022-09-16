# Hit the Target Game
import turtle
import math

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT ** 2 + SCREEN_HEIGHT ** 2) / 2)

TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target

PROJECTILE_SPEED = 1  # Projectile's animation speed

EAST = 0              # Angle of east direction
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

pen = turtle.Pen()

# Draw the target.
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
pen.pendown()
pen.setheading(EAST)
pen.forward(TARGET_WIDTH)
pen.setheading(NORTH)
pen.forward(TARGET_WIDTH)
pen.setheading(WEST)
pen.forward(TARGET_WIDTH)
pen.setheading(SOUTH)
pen.forward(TARGET_WIDTH)
pen.penup()

is_hit = False
while not is_hit: 
    # Center the turtle.
    pen.home()
    pen.showturtle()
    pen.speed(PROJECTILE_SPEED)

    # Get the angle and force from the user.
    angle = int(input("Enter the projectile's angle 0-360: "))
    distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}): '))

    # Set the heading.
    pen.setheading(angle)

    # Launch the projectile.
    pen.pendown()
    pen.forward(distance)

    xcor = pen.xcor()
    ycor = pen.ycor()

    # Did it hit the target?
    is_in_x = ((xcor >= TARGET_LLEFT_X) and 
        (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
    is_in_y = ((ycor >= TARGET_LLEFT_Y) and
        (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
    is_hit = is_in_x and is_in_y

    # show message
    if is_hit:
        print('Target hit!')
    else:
        print('You missed the target.')

turtle.done()