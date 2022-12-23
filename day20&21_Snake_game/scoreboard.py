from turtle import Turtle
FONT = ("Arial", 16, "normal")
ALIGNMENT = "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("highscores.txt") as file_var:
            current_highscore = file_var.read()
        self.write(f"Score: {self.score} High score: {current_highscore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscores.txt", "w") as file_var:
                file_var.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


