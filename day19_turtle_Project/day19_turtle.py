from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")


# def move_forward():
#     timmy.fd(100)
#
#
# screen.listen()
# screen.onkey(move_forward, "space")
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)
timmy.width(7)
def move_forward():
    change_color()
    timmy.fd(30)
def move_backward():
    change_color()
    timmy.backward(30)

def turn_right():
    timmy.right(5)

def turn_left():
    timmy.left(5)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
