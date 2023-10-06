import colorgram

# colors = colorgram.extract("image.jpg", number_of_colors=30)
# color_list = []
#
# for item in range(len(colors)):
#     current_color = colors[item]
#     rgb = current_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color = (r, g, b)
#     color_list.append(color)

import random
import turtle as t


color_list = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
          (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
          (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
          (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
          (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

tim.speed("fastest")
def draw_line(number_dots):
    for i in range(number_dots):
        tim.penup()
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        tim.penup()
        # tim.forward(10)

draw_line(10)

for item in range(10):

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    draw_line(10)


screen = t.Screen()
screen.exitonclick()