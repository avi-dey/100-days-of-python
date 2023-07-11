# challenge 2
from turtle import Turtle, Screen

tim = Turtle()

tim.pen(fillcolor="green", pencolor="red", pensize=5, speed=1)

for _ in range(4):
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)


window = Screen()
window.exitonclick()
