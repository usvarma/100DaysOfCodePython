from turtle import Turtle, Screen
import random

screen = Screen()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange"]
turtles = []
step_sizes = [x * 2 for x in range(5)]


def init_turtles():
    for i in range(6):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colors[i - 1])
        turtles.append(t)


def setup_screen():
    screen.setup(width=800, height=600)
    return screen.textinput("Who's gonna win the race?", "Pick a turtle color to win the race")


def place_turtles():
    xpos = -380
    ypos = 0

    for i in range(int(len(turtles) / 2)):
        ypos += 40
        turtles[i].goto(xpos, ypos)
    ypos = 0
    for i in range(int(len(turtles) / 2), len(turtles)):
        ypos -= 40
        turtles[i].goto(xpos, ypos)


def move_turtles():
    winner = ""
    game_over = False

    while not game_over:
        for t in turtles:
            if t.xcor() >= (screen.window_width() / 2):
                winner, _ = t.color()
                game_over = True
                break
            t.fd(random.choice(step_sizes))
    return winner


def turtle_race():
    user_bet = setup_screen()
    init_turtles()
    place_turtles()
    winner = move_turtles()
    if user_bet == winner:
        print("You win!")
    else:
        print(f"You lose! Turtle with {winner} color wins!")
    screen.exitonclick()


if __name__ == '__main__':
    turtle_race()
