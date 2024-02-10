from turtle import Turtle, register_shape
import random

STARTING_POSITION = (280, 0)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100
START_X = 300
register_shape("car.gif")


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def cars(self):
        random_num = random.randint(1, 10)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("car.gif")
            new_car.turtlesize(stretch_wid=0.5, stretch_len=0.5)
            new_car.setheading(180)
            new_car.penup()
            new_car.color("black")
            new_car.color(random.choice(COLORS))
            y_cor = random.randrange(-250, 250)
            new_car.goto(START_X, y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
