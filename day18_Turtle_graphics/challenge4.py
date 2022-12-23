import turtle
from turtle import Turtle, Screen
from random import choice, randint
tim = Turtle()
turtle.colormode(255)

list_of_directions = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0,255)
    b = randint(0,255)
    rand_color = (r, g, b)
    return rand_color


for i in range(200):
    tim.color(random_color())
    tim.width(20)
    tim.speed(100)
    tim.forward(50)
    tim.setheading(choice(list_of_directions))

myscreen = Screen()
myscreen.exitonclick()
