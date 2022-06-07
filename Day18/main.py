from turtle import Turtle, Screen
import random

colors = [x for x in range(256)]


def get_random_rgb():
    r = random.choice(colors)
    g = random.choice(colors)
    b = random.choice(colors)
    return r, g, b


if __name__ == '__main__':
    t = Turtle()
    screen = Screen()
    """for i in range(24):
        drawing_turtle.left(15)
        drawing_turtle.fd(100)
        drawing_turtle.left(45)
        drawing_turtle.fd(10)
        drawing_turtle.left(90)
        drawing_turtle.fd(10)
        drawing_turtle.left(45)
        drawing_turtle.fd(100)
    """
    """for i in range(0, 100, 10):
        t.fd(10)
        if t.pencolor() == "black":
            t.pencolor("white")
        else:
            t.pencolor("black")"""
    """total_degrees = 360

    for i in range(3, 11):
        turn_angle = total_degrees / i
        t.pencolor(random.choice(COLORS))
        for turns in range(i):
            t.fd(100)
            t.left(turn_angle)
"""

    """ step_size = 40
    angles = [0, 90, 180, 270]
    t.pensize(10)
    t.speed(10)
    screen.colormode(255)
    for i in range(1000):
        t.setheading(random.choice(angles))
        t.pencolor(get_random_rgb())
        t.forward(step_size) """


def draw_spirograph(gap_size):
    screen.colormode(255)
    t.speed("fastest")
    for i in range(int(360 / gap_size)):
        t.left(gap_size)
        t.pencolor(get_random_rgb())
        t.circle(100)


draw_spirograph(3)

screen.exitonclick()
