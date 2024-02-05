import turtle
from turtle import Turtle, Screen

import random

should_continue = True
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")

turtle.colormode(255)


def change_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    change_color = (R, G, B)
    return change_color
timmy.speed(0)
while should_continue:
    timmy.color(change_color())
    timmy.circle(150)

    timmy.right(3)
    if timmy.heading()==0:
        should_continue=False



# turtle.home()
# turtle.position()
# (0.00,0.00)
# turtle.heading()
# 0.0
# turtle.circle(50)
# turtle.position()
# (-0.00,0.00)
# turtle.heading()
# 0.0
# turtle.circle(120, 180)  # draw a semicircle
# turtle.position()
# (0.00,240.00)
# turtle.heading()
# 180.0
screen.exitonclick()