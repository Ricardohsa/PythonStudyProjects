class Snake:
    from turtle import Turtle

    snake = Turtle()
    def __init__(self):
        self.shape("square")
        self.color("white")
        self.shapesize(1, 3)
        self.penup()


    def grow(self):
        self.snake.shapesize(1, self.snake.shapesize()[1] + 1)

    def move(self):
        self.snake.forward(10)

