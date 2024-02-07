import colorgram
from turtle import Turtle, Screen

import random
new_list = [(202, 164, 109),(150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.hideturtle()


import turtle

timmy.speed(0)

timmy.penup()

turtle.colormode(255)
timmy.backward(200)
timmy.left(90)
timmy.forward(300)
timmy.left(90)
timmy.left(90)
timmy.left(90)


def one_row():
    for n in range(10):
        timmy.fd(50)
        timmy.fillcolor(random.choice(new_list))

        timmy.begin_fill()

        timmy.circle(10)

        timmy.end_fill()
        timmy.penup()



one_row()
timmy.setheading(270)
for n in range(9):

    timmy.fd(50)

    if timmy.heading()==0:
        timmy.backward(100)
        one_row()
        timmy.setheading(270)
    elif timmy.heading()==270:
        timmy.setheading(180)
        timmy.backward(50)
        one_row()
        timmy.setheading(270)
        timmy.fd(100)
        timmy.setheading(0)

screen.exitonclick()
