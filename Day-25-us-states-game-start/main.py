import csv
from turtle import Turtle, Screen, mainloop
import pandas

screen = Screen()
turtle = Turtle()
turtle.hideturtle()
states = Turtle()

screen.title("U.S States Game")

screen.addshape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")
with open("50_states.csv", "r") as file:
    states.hideturtle()
    data = pandas.read_csv(file)
    data_list = data.state.tolist()

states.penup()
n = 0
correct_answer = []
game_on = True
while game_on:

    score = len(correct_answer)
    if score == 50:
        game_on = False
    answer = screen.textinput(title=f"{score}/50 "" Guess IT!", prompt="Whats a State Name").title()
    if answer == "Exit":
        break
    if answer in data_list and answer not in correct_answer:
        coordinates = data[data["state"] == answer]

        states.goto(x=int(coordinates.x), y=int(coordinates.y))
        states.write(arg=answer)
        correct_answer.append(answer)

print(correct_answer)

# states left to learn . csv
for num in correct_answer:
    data_list.remove(num)
data = pandas.DataFrame(data_list)


data.to_csv("left_states.csv")
