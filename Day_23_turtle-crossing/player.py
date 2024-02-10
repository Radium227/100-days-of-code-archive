from turtle import Turtle, register_shape

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
register_shape("turtle.gif")

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle.gif")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
        # y_cor = self.ycor() + MOVE_DISTANCE
        # if self.ycor() <= FINISH_LINE_Y:
        #     self.goto(x=self.xcor(), y=y_cor)

    def reset_pos(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
