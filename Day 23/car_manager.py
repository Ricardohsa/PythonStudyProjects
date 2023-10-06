import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-250, 280)
            new_car.goto(x= 300, y= random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    # def restart(self):
    #     self.goto(x=self.xcor, y=self.ycor)

    def level_up(self):
        self.speed += MOVE_INCREMENT

    # def reset_game(self):
    #     # self.goto(x=self.xcor, y=self.ycor)
    #     self.forward(MOVE_INCREMENT)


