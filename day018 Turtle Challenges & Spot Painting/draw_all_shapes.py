# challenge 3

# logic: 360 / number of side = exterior angles (any regular shape)
# 360 / 3 = 120 (regular triangles)
# 360 / 4 = 90 (squares)
# 360 / 5 = 72 (pentagon)
# and so on

from turtle import Turtle, Screen
from random import randint

tim = Turtle()

tim.pensize(5)

window = Screen()
window.colormode(255)  # gives us access to all 0 to 255 colors in a screen

for i in range(3, 11):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))  # rgb
    for _ in range(i):
        tim.forward(100)
        tim.left(int(360 / i))


window.exitonclick()
