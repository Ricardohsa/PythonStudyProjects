from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
final_position = (220.00,0.00)
is_race_on = False
colors = ["blue", "red", "green", "yellow", "orange", "black"]
y_postion = [-100, -50, 00, 50, 100, 150]
speed_list = [10, 15, 5, 25, 30, 35, 45]
all_turtles = []

user_bet = screen.textinput("Color", "Which Turtle will win the race? Enter a color:")


# def race():
#     for speed in range(0,6):
#         new_turtle.forward(speed_list[speed])

def create_turtles():
    for turtle_index in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(-225.00, y_postion[turtle_index])
        all_turtles.append(new_turtle)

create_turtles()

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0,15)
    turtle = random.choice(all_turtles)
    turtle.forward(rand_distance)
    current_position = turtle.position()

    if current_position >= final_position:
        is_race_on = False
        color = turtle.pencolor()

        if color == user_bet:
            print("You Win")
        else:
            print("You lost:")

screen.listen()
screen.exitonclick()










