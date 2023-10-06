from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG = "black"
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG)
screen.title("PONG")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard(150, 280)
l_score = Scoreboard(-150, 280)

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l_score.uppdate()

    if ball.xcor() < -380:
        ball.reset_position()
        r_score.uppdate()

screen.exitonclick()
