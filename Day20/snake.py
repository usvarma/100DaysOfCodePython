from turtle import Turtle


class Snake:

    def __init__(self):
        self.xpos = -20
        self.snake = []
        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(self.xpos, 0)
            self.snake.append(t)
            self.xpos -= 20

    def move(self, screen):
        for i in range(len(self.snake) - 1, 0, -1):
            xpos = self.snake[i - 1].xcor()
            ypos = self.snake[i - 1].ycor()
            self.snake[i].goto(xpos, ypos)
        self.snake[0].fd(20)

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def left(self):
        self.snake[0].setheading(180)

    def right(self):
        self.snake[0].setheading(360)
