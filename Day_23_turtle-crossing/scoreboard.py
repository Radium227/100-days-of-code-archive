from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1

    def increase(self):
        self.score += 1

    def record(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Score:{self.score}", align="center", font=(FONT))

    def gameover(self):
        self.clear()
        self.goto(0, 40)
        self.write("GAME OVER", align="center", font=("Courier", 20, "bold"))
        self.goto(0, 10)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 14, "normal"))
