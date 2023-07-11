# challenge 4

# random walk using random colors challenge
# applications of random walk: https://en.wikipedia.org/wiki/Random_walk#Applications

from turtle import Turtle, Screen
import random


def random_color_generate():
    """returns tuple of rgb colors"""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# def move_left(dist):
#     tim.left(90)
#     tim.forward(dist)
#
#
# def move_right(dist):
#     tim.right(90)
#     tim.forward(dist)


# def random_move():
    # return random.choice([tim.forward(20), tim.backward(20), tim.move_left(20), tim.move_right(20)])


tim = Turtle()
window = Screen()

tim.speed(1)
window.colormode(255)  # gives the window access to 0 to 255 colors

for _ in range(100):
    color_tuple = random_color_generate()
    tim.pen(pencolor=color_tuple, pensize=10, speed=1)

    move = random.randint(1, 4)
    if move == 1:
        tim.forward(40)
    elif move == 2:
        tim.backward(40)
    elif move == 3:
        tim.left(90)
        tim.forward(40)
    else:
        tim.right(90)
        tim.forward(40)

window.exitonclick()
