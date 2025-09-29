# Importing section
from turtle import Turtle
from random import choice, randint
# Constant Variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a car at the right edge with a random y-position."""
        # 1 in 6 chance to create a car each time this is called
        if randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            random_y = randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars leftwards by the current car speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Increase the speed of all cars (call when level up)."""
        self.car_speed += MOVE_INCREMENT