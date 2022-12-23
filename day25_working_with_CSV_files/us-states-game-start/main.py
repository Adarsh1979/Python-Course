import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
count = 0

while count < 50:
    answer_state = screen.textinput(title=f"{count}/50 States correct", prompt="What's another states name ?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        count += 1
        text = Turtle()
        text.penup()
        text.hideturtle()
        answer = data[data["state"] == f"{answer_state}"]
        guessed_states.append(answer_state)
        text.goto(int(answer.x), int(answer.y))
        text.write(f"{answer_state}")

