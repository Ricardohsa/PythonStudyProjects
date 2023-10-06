from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.high_score = self.get_high_score()
        self.goto(0, 280)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(arg=f"Score: {self.score} High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_data(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            data = file.read().splitlines()
            high_score = int(data[-1])
        return high_score


    def update_data(self, high_score):
        with open("data.txt", "a") as file:
            file.write(f"\n {high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
