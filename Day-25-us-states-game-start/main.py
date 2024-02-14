import csv
from turtle import Turtle, Screen, mainloop
import pandas

screen = Screen()
turtle = Turtle()
states = Turtle()

screen.title("U.S States Game")

screen.addshape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")

states.hideturtle()
states.penup()
n = 0
correct_answer = []
game_on = True
while game_on:

    with open("50_states.csv", "r") as file:
        data = pandas.read_csv(file)
        data_list = data.state.tolist()
        score = len(correct_answer)
        answer = screen.textinput(title=f"{score}/50 "" Guess IT!", prompt="Whats a State Name").title()
        if answer in data_list and answer not in correct_answer:

                coordinates = data[data["state"] == answer]

                states.goto(x=int(coordinates.x), y=int(coordinates.y))
                states.write(arg=answer)
                correct_answer.append(answer)

    print(correct_answer)
    if score == 50:
        game_on = False

print(correct_answer)

mainloop()
