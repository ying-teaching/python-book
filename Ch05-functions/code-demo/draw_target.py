import turtle

TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target

# Task2: Draw the target square whose
# bottome left corner (100, 250) with side length 25
def draw_target_square():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()

    directions = [0, 90, 180, 270]
    for direction in directions:
        turtle.setheading(direction)
        turtle.forward(TARGET_WIDTH)

    turtle.penup()