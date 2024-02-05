import time
from turtle import Turtle,Screen
from typing import List
from snake import Snake



screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.reset,"Q")



should_continue=True

while should_continue:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()









screen.exitonclick()