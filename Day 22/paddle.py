from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_cor):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=paddle_cor[0], y=paddle_cor[1])

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycor)
