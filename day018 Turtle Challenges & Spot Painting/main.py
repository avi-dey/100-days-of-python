# import colorgram
import random
# TODO: get all the colors from the image in a list of tuples format using colorgram package

# colors = colorgram.extract("damien-hirst-spot-painting.jpg", 30)
#
# color_list = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     color_list.append((r, g, b))
#
# print(color_list)

from turtle import Turtle, Screen
import random

# extracted these colors with the help of colorgram
colors = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
          (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
          (174, 135, 163),
          (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
          (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

tim = Turtle()

tim.penup()  # don't draw path
tim.hideturtle()  # don't show pen

# print a matrix of dots
x = -250
y = -250

screen = Screen()
screen.colormode(255)

tim.setpos(x, y)  # start pos
for i in range(10):
    for j in range(10):
        random_color = random.choice(colors)
        tim.dot(20, random_color)
        tim.fd(50)
    y += 50
    tim.setpos(x, y)


screen.exitonclick()
