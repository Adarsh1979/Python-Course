import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

screen = Screen()       # creating a screen for the game
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()     # used listen() method to respond to keypress i.e. Up arrow key
screen.onkey(player.go_up, "Up")        # when Up is pressed, go_up() will be called

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:        # here we are detecting the collision with cars
        if player.distance(car) < 20:       # comparing the distance of player from each car in the list of all_cars
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish_line():      # If player reaches at the top,
        car_manager.level_up()          # level increases and speed of cars also increases
        score_board.increase_score()

screen.exitonclick()
