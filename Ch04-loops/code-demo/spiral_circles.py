# This program draws a design using repeated circles.
import turtle

# Named constants
NUM_CIRCLES = 36    # Number of circles to draw
RADIUS = 100        # Radius of each circle
ANGLE = 10          # Angle to turn
ANIMATION_SPEED = 0 # Animation speed

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()

# Question, how do we draw circles in 
# red, green, and blue color alternatively?



## TIPS: 
# COLORS = ['red', 'green', 'blue']
# color_index = x % len(COLORS)
# color = COLORS[color_index]
# turtle.color(color)
