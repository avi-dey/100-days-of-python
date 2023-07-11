from turtle import Turtle, Screen

tim = Turtle()

tim.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=5)

tim.begin_fill()  # call this function before filling a shape
tim.circle(80)
tim.end_fill()  # call this function after filling a shape

screen = Screen()
screen.exitonclick()
