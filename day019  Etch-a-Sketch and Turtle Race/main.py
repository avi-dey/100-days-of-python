# Turtle race
from turtle import Turtle, Screen
import random


def random_speed():
    return random.randint(0, 10)  # 10 is inclusive


race_is_on = True
all_turtles = []  # we will store the turtle instances here
y_coordinates = [-100, -60, -20, 20, 60, 100]  # separated by 30 pixels
colors = ["violet", "indigo", "blue", "green", "yellow", "orange"]

screen = Screen()
screen.setup(width=700, height=400)

user_bet_color = screen.textinput(title="Turtle Race Bet", prompt=f"Which turtle would win: \nOptions: {colors} \n")
while user_bet_color not in colors:
    print("❌ INVALID INPUT ❌")
    user_bet_color = screen.textinput(title="Turtle Race Bet", prompt=f"Which turtle would win: \nOptions: {colors} \n>")

for i in range(6):
    new_turtle = Turtle("turtle")
    all_turtles.append(new_turtle)

    new_turtle.penup()
    new_turtle.fillcolor(colors[i])
    # the size of the turtle by default is 20px by 20px
    new_turtle.goto(x=-270, y=y_coordinates[i])

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 270:
            turtle.write("I won", font=('Arial', 16, 'normal'))
            winner_color = turtle.fillcolor()

            if user_bet_color == winner_color:
                print(f"Correct bet! The winner turtle is {winner_color}")
            else:
                print(f"Wrong bet. The winner turtle is {winner_color}")

            race_is_on = False
            break
        turtle.forward(random_speed())


screen.exitonclick()

