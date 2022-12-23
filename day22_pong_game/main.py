from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreBoard1 = Scoreboard(-70, 270, "Adarsh")
scoreBoard2 = Scoreboard(70, 270, "Sahil")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.increaseSpeed)
    screen.update()
    ball.move()
    # detecting collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 345) or (ball.distance(l_paddle) < 40 and ball.xcor() < -345):
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.reset_position()
        scoreBoard1.increaseScore()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreBoard2.increaseScore()

screen.exitonclick()