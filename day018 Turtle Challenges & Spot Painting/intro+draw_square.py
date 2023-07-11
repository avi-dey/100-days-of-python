# intro + challenge 1
from turtle import Turtle, Screen

avi = Turtle()
avi.shape("turtle")
# avi.color("green")  # turtle color + pen color as a whole
avi.fillcolor("red")  # turtle color
avi.pencolor("blue")  # pen color

avi.speed(1)
for _ in range(4):
    avi.forward(100)
    avi.left(90)


screen = Screen()
screen.exitonclick()
