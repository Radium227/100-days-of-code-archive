from turtle import Turtle

import food
from food import Food



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-10,y=260)
        self.early=0


    def track(self):
        self.write(arg=f'Score : {self.early} ', move=False, align='center', font='Arial')

    def gameover(self):
        self.goto(0,0)
        self.write(arg='GAME OVER!', font=('arial',15,'bold'), align='center')
