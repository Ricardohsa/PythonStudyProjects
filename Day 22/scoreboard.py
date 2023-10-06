from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, 'normal')
class Scoreboard(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.clear()
        self.penup()
        self.goto(xcor, ycor)
        self.score = 0
        self.uppdate()


    def uppdate(self):
        self.clear()
        self.color("white")
        self.write(arg=f"Score: {self.score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.score += 1