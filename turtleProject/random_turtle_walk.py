import turtle
from turtle import Turtle, Screen

import random

direction = ["left", "right", "forward"]

turtle.colormode(255)
def change_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    change_color=(R,G,B)
    return change_color

angle = [0, 90, 180, 270]
should_continue = True
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.width(9)

while should_continue:
    timmy.color(change_color())

    timmy.setheading(random.choice(angle))
    timmy.fd(20)
    timmy.left(random.choice(angle))
    timmy.speed(0)

screen.exitonclick()

# from turtle import Turtle
# from random import random
#
# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
#
# t.screen.mainloop()
