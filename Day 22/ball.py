from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)
        self.pendown()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def ball_down(self):
        self.penup()
        self.goto(0,0)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.bounce_x()
        self.move_speed = 0.1