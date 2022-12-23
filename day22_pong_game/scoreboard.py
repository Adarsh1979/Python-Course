from turtle import Turtle
FONT = ("Arial", 16, "normal")
ALIGNMENT = "right"


class Scoreboard(Turtle):
    def __init__(self, xcor, ycor, player_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(xcor, ycor)
        self.score = 0
        self.playerName = player_name
        self.write(f"{player_name}: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"{self.playerName} Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
