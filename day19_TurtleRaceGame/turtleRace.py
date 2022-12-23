from turtle import Turtle, Screen
from random import randint

s = Screen()
s.setup(width=700, height=600)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x_pos = -300
y_pos = -160 

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color_list[i])
    tim.penup()
    tim.goto(x=x_pos, y=y_pos)
    all_turtles.append(tim)
    y_pos += 50


is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 325:
            is_race_on = False
            tcolor = turtle.pencolor()
            if user_bet.lower() == tcolor:
                print(f"You've won! The {turtle.pencolor()} turtle is winner.")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is winner.")

        turtle.forward(randint(0,10))
s.exitonclick()