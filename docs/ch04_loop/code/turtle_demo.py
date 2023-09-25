import turtle

# don't name the file a turtle.py -- it causes a name conflict error.

# Named constants
NUM_CIRCLES = 36  # Number of circles to draw
RADIUS = 100  # Radius of each circle
ANGLE = 10  # Angle to turn
ANIMATION_SPEED = 0  # Animation speed
COLORS = ["red", "green", "blue"]

t = turtle.Turtle()
t.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
color_index = 0
for x in range(NUM_CIRCLES):
    t.pencolor(COLORS[color_index])
    t.circle(RADIUS)
    t.left(ANGLE)

    color_index += 1
    if color_index >= len(COLORS):
        color_index = 0

t.screen.mainloop()
