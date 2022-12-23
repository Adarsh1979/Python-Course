from turtle import Turtle, Screen
from random import choice
tim = Turtle()
list_of_colors = ["red", "blue", "yellow", "grey", "purple", "cyan"]


def drawshape(no_of_sides):
    angle = 360/no_of_sides
    tim.speed(0)
    tim.width(10)
    tim.color(choice(list_of_colors))
    for _ in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    drawshape(i)

myscreen = Screen()
myscreen.exitonclick()
