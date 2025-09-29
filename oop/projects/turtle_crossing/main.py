# Importing section
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set-up
screen = Screen()
screen.setup (width= 600, height= 600)
screen.bgcolor ("black")
screen.tracer (0)
player = Player ()
car__manger = CarManager ()
score_board = Scoreboard ()

# Keep game on until collides with a car
game_is_on = True
while game_is_on:
    time.sleep (0.1)
    screen.update ()
    screen.listen ()
    screen.onkey (fun= player.move_forward, key= "Up")
    screen.onkey (fun= player.move_back, key= "Down")
    car__manger.create_car ()
    car__manger.move_cars ()
    if player.ycor () > 300:
        player.back ()
        car__manger.increase_speed ()
        score_board.increase_level ()
        score_board.update_scoreboard ()

    for car in car__manger.all_cars:
        if player.distance (car) < 20:
            game_is_on = False
            score_board.game_over ()
            break

screen.exitonclick ()