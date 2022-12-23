from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:       # this class will create and move the cars and also increase the speed if the player levels up

    def __init__(self):
        self.all_cars = []      # for accessing each car (to move), we have stored it in this all_cars list
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_num = random.randint(1, 8)
        if rand_num == 1 or rand_num == 5:      # this if block is reducing the number of cars generating in while loop
            # of email_challenge.py file. If the rand_num generated is 1 or 5, then only we are creating car. So it reduces the no.
            # of cars in each iteration of while loop
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)     # here we are shifting each car to (300,random_y) so that it starts off from
            # left side
            self.all_cars.append(new_car)       # storing each car in all_cars list so as to move each car backward

    def move(self):
        for car in self.all_cars:       # moving each car backward by car_speed distance which gets incremented after
                                            # each level up
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
