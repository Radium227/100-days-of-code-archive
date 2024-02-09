from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()


        self.shape("square")
        self.color("white")

        self.turtlesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(position)



    def go_up(self):
            y_cor = self.ycor() + 40
            if self.ycor()<240 :
                self.goto(x=self.xcor(), y=y_cor)


    def go_down(self):
            y_cor = self.ycor() - 40
            if self.ycor() >-240:
                self.goto(x=self.xcor(), y=y_cor)
