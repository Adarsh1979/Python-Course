from turtle import Turtle

FONT = ("Courier", 24, "normal")

# This class is creating a scoreboard with the help of Turtle class


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):        # this method will write score on the turtle
        self.clear()        # to avoid overwriting, we have cleared the previously written score
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):       # increasing the score attribute after level up
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
