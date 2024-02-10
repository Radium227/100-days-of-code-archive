import time

from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)

turtle=Turtle()
turtle.penup()
turtle.hideturtle()
screen.tracer(0)

def straight():
    turtle.width(3)
    position = 300
    draw = True
    while draw:

        position-=300
        turtle.pendown()
        turtle.goto(position, turtle.ycor())
        turtle.penup()
        if turtle.xcor() == -300:
            draw = False


def dotted():
    position = 300
    draw = True
    while draw:
        position-=25
        turtle.width(2)
        turtle.pendown()
        turtle.goto(position,turtle.ycor())
        turtle.penup()
        position-=25
        turtle.goto(position,turtle.ycor())
        print(position)
        if turtle.xcor()==-300:
            draw=False

turtle.goto(300,-70)
dotted()
turtle.goto(300,130)
dotted()
turtle.goto(300,80)
straight()
turtle.goto(300,180)
straight()
turtle.goto(300,-20)
straight()
turtle.goto(300,-130)
straight()
turtle.goto(300,-250)
straight()

player = Player()
screen.listen()
car_manager = CarManager()

screen.onkeypress(player.up, "Up")

n = 0.03
game_is_on = True
while game_is_on:
    time.sleep(n)
    screen.update()
    car_manager.cars()
    car_manager.move()
    scoreboard.record()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.gameover()
    # finish line
    if player.ycor() >= 290:
        player.reset_pos()

        scoreboard.increase()

        n -= 0.01

screen.exitonclick()
