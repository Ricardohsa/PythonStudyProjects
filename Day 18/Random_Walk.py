import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("circle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "black", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


for i in range(150):
    tim.width(15)
    tim.forward(50)
    tim.setheading(random.choice(direction))
    tim.speed("fastest")
    tim.color(random.choice(colours))




screen = Screen()
screen.exitonclick()
