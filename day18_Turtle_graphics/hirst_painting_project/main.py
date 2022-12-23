# import colorgram
# colors = colorgram.extract('hirstimage.jpg', 20)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_list.append(color_tuple)
# print(rgb_list)

from turtle import Turtle, Screen
import turtle
from random import choice

turtle.colormode(255)
color_list = [(33, 3, 238), (61, 3, 60),
              (250, 126, 2), (3, 251, 4), (243, 135, 31), (245, 3, 0), (251, 250, 29), (206, 5, 70), (26, 242, 29),
              (55, 7, 252), (254, 254, 0), (151, 56, 85), (102, 75, 227), (215, 6, 90), (215, 53, 83), (97, 245, 98)]

t = Turtle()
t.speed("fastest")
t.hideturtle()
pos_x = t.xcor() - 200.0
pos_y = t.ycor() - 200.0

for i in range(10):
    t.penup()
    t.setx(pos_x)
    t.sety(pos_y)
    for j in range(10):
        t.dot(20, choice(color_list))
        t.forward(50)


    pos_y += 50


myscreen = Screen()
myscreen.exitonclick()