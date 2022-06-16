from turtle import Turtle, Screen
from snake import Snake

screen = Screen()


def setup_screen():
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.listen()

    return


if __name__ == '__main__':
    setup_screen()
    snake = Snake()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_over = False

    while not game_over:
        screen.update()
        snake.move(screen)
    screen.exitonclick()
