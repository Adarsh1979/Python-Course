import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# because of this tracer() the screen can be hidden for sometimes and can be shown at any time by using update() method
# this helps to skip the frames where segments are following head and moving as a full snake(which will not make
# the game look good)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()       # This is to set keybindings with our game
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()        # Because of this move() and while loop all segments of snake will follow previous segments

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    #                                           Note: here segments[1:] is called slicing which slices the given list
    # detecting collision with tail              from a certain index to a certain index
    for segment in snake.segments[1:]:      # Because if we loop through whole list of segments, first segment is
        if snake.head.distance(segment) < 10:    # head only and its distance from head would be zero and game will
            scoreboard.reset_scoreboard()                # be over
            snake.reset_snake()

screen.exitonclick()
