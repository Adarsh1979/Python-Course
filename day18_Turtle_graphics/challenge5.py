import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0,255)
    b = randint(0,255)
    rand_color = (r, g, b)
    return rand_color


t = Turtle()
t.speed(0)
t.width(1)
deflection = 5
for i in range(int(360/deflection)):
    t.color(random_color())
    t.circle(200)
    t.left(deflection)

myscreen = Screen()
myscreen.exitonclick()