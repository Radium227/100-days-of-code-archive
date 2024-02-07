import time
from turtle import Screen
from scoreboard import Score
from snake import Snake
from food import Food

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
score=Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



should_continue = True

while should_continue:


    screen.update()
    time.sleep(0.1)
    screen.onclick("w")
    snake.move()

    score.track()

    if snake.head.distance(food) < 15:
        score.clear()
        snake.bigger()
        food.refresh()
        score.early+=1
    if snake.head.xcor()> 285 or snake.head.ycor()> 285 or snake.head.xcor()< -285 or snake.head.ycor()< -285:
        should_continue=False
        score.gameover()

#collision

    for segment in snake.snake[1:]:

        if snake.head.distance(segment) <10:
            should_continue=False
            score.gameover()


screen.exitonclick()
