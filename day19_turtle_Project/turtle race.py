import turtle
from turtle import Turtle, Screen
import random

new_list = []
screen = Screen()
colors = ["green", "blue", "red", "yellow", "orange", "purple"]
continue_game = True
turtle.penup()
turtle.hideturtle()
for n in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(n)
    new_list.append(new_turtle)
    new_turtle.penup()

screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet", prompt="Enter the color of turtle you want to bet on: ")
height = 85
width = -225
for n in range(0, 6):
    new_list[n].goto(x=width, y=height)
    height -= 35

print(choice)

while continue_game:
    x = random.choice(new_list)

    if x.xcor() > 222:

        continue_game = False

    else:
        random.choice(new_list).fd(random.randint(0, 6))

if x.xcor() >= 222:
    if x.pencolor() == choice:
        print(f"Congratulations {x.pencolor()} won the race!")
    else:
        print(f"You lost the bet! {x.pencolor()} won the race")

screen.exitonclick()
