# challenge 5

import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)  # makes all the 255 shades accessible


def random_rgb_generate():
    """returns a tuple of rgb color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.pen(pensize=3, speed="fastest")

count = 0


# logic : if we change angle everytime by 5 degrees
# then (360/5)degrees = 72 revolutions
# after 72 rotations we go back to initial 0 degrees position
# let's generalise this logic
def draw_spirograph(degrees, circle_radius=100):
    revolutions = int(360/degrees)
    for _ in range(revolutions):
        tim.pencolor(random_rgb_generate())
        tim.circle(circle_radius)
        tim.left(degrees)


draw_spirograph(10, 100)

screen.exitonclick()
