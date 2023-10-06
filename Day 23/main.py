import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
score = Scoreboard()


car_manager = CarManager()


screen.onkey(fun=turtle.cross_street, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            turtle.back_initial_position()
            score.game_over()
            # game_is_on = False

    if turtle.ycor() >= 280:
        score.update_level()
        turtle.back_initial_position()
        car_manager.level_up()





