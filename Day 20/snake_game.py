from turtle import Turtle, Screen
from Snake import Snake

# snake = Turtle()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

snake = Snake()



screen.onkey("UP")

game_is_on = True

while game_is_on:
  snake.move()




screen.exitonclick()

