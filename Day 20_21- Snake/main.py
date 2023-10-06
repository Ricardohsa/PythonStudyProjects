import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.Up)
screen.onkey(key="Down", fun=snake.Down)
screen.onkey(key="Left", fun=snake.Left)
screen.onkey(key="Right", fun=snake.Right)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset()

screen.exitonclick()
