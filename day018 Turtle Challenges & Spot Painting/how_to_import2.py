import turtle as t

tim = t.Turtle()

tim.color("green")
tim.speed(1)

for _ in range(8):
    tim.forward(100)
    tim.left(45)
tim.write("octagon printed")

screen = t.Screen()
screen.exitonclick()
