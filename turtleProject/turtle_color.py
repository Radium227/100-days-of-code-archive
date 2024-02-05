from turtle import Turtle, Screen

import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


should_continue = True

# elsa.color(random.choice(colours))
side = 2

while should_continue:
    side += 1
    change_color()
    if side == 11:
        should_continue = False
    else:
        angle = 360 / side
        for n in range(side):
            timmy.forward(100)
            timmy.right(angle)

screen.exitonclick()
