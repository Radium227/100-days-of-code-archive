from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen=Screen()
score=Score()



r_paddle=Paddle((355,0))
l_paddle=Paddle((-355,0))

ball=Ball()
turtle=Turtle()
turtle.color("white")
turtle.penup()
turtle.goto(0,290)
turtle.setheading(270)
turtle.hideturtle()
screen.tracer(0)
turtle.width(2)
for n in range(29):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
score.update_score()


screen.setup(height=600,width=800)


screen.bgcolor("black")

screen.title("Pong")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down" )

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s" )
n=0.04
continue_game=True


while continue_game:
    screen.update()

    time.sleep(n)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle)<55 and ball.xcor() >330 or  ball.distance(l_paddle)<55 and ball.xcor()< -330:
        ball.paddle_crash()
        n-=0.003
    if ball.xcor()>385:
        score.increase_l()
        score.update_score()
        ball.reset()
        n=0.04
    if ball.xcor() < -385:
        score.increase_r()
        score.update_score()
        ball.reset()
        n=0.04







screen.exitonclick()