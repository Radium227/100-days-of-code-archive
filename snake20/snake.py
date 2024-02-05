from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        position = 0
        for n in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=position, y=0)
            position -= 20
            self.snake.append(new_turtle)



    def move(self):

        for n in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[n - 1].xcor()
            new_y = self.snake[n - 1].ycor()
            self.snake[n].goto(new_x, new_y)
        self.snake[0].fd(20)

    def up(self):
        if self.snake[0].heading()!=DOWN:
                self.snake[0].setheading(UP)
    def  down(self):
        if self.snake[0].heading() != UP:
                self.snake[0].setheading(DOWN)
    def left(self):
        if self.snake[0].heading() != RIGHT:
                self.snake[0].setheading(LEFT)
    def right(self):
        if self.snake[0].heading() != LEFT:
                self.snake[0].setheading(RIGHT)
    def reset(self):
        self.snake[0].reset()


