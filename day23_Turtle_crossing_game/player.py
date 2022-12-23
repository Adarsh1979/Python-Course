# This file is for generating a player i.e. turtle and moving it in upward direction

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):  # Player class is inheriting from Turtle so that we can use Player as a Turtle also
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):  # this function will be triggered when up key is pressed (in the email_challenge.py)
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):  # this function is for checking whether the player has reached as the top or not
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
            return True  # we are returning true coz we want to increase speed of cars as soon as the player reaches
            # the finishline (inside the if statement in email_challenge.py)
