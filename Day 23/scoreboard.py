from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.goto(-280,250)
        self.level = 1
        self.write(arg=f"Level: {self.level} ", align="left",  font=FONT)
        self.hideturtle()

    def update_level(self):
        self.level += 1
        self.clear()
        self.penup()
        self.write(arg=f"Level: {self.level} ", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(-0, 0)
        self.write(arg="GAME OVER ", align="center", font=FONT)


