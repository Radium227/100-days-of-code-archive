from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0



    def increase_l(self):
        self.l_score+=1
    def increase_r(self):
        self.r_score+=1
    def update_score(self):
        self.clear()
        self.goto(-60, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(60, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))
