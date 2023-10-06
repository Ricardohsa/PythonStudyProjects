import random
import turtle as t


tim = t.Turtle()
t.colormode(255)
tim.shape("circle")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "black", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)



for i in range(50):
    tim.width(15)
    tim.forward(50)
    tim.setheading(random.choice(direction))
    tim.speed("fastest")
    tim.pencolor(random_color())




screen = t.Screen()
screen.exitonclick()