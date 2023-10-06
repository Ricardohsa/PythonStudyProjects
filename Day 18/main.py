import random
from turtle import Turtle, Screen

tim = Turtle()
tim.color("#9ACD32")
tim.shapesize(2, 2)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "black", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_square(move_forward, turn_right):
    for item in range(4):
        tim.forward(move_forward)
        tim.right(turn_right)


def draw_dashed_line():
    tim.pensize(5)
    for _ in range(30):
        tim.forward(5)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draq_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def change_color():
    for color in colours:
        tim.color(color)


for _ in range(3, 11):
    draq_shapes(_)
    tim.color(random.choice(colours))

draq_shapes(10)

screen = Screen()
screen.exitonclick()
