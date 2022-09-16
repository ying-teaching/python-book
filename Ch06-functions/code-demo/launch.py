import turtle

PROJECTILE_SPEED = 1  # animation speed

def launch_turtle(angle, distance):
    turtle.home()
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED) 

    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(distance)