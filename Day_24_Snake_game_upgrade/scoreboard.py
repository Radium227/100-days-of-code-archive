from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt") as file:
    CONTENTS=int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = CONTENTS
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))


        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align=ALIGNMENT, font=18)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
