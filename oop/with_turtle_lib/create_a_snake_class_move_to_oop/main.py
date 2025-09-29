# Importing section
import time
from turtle import Screen, Turtle
from snake import Snake

# Creating object for screen and setup it.
screen = Screen ()
screen.setup (width= 1000, height= 1000)
screen.bgcolor ("black") # Change background color to black.
screen.title ("My Snake Game")
screen.tracer (0) # Hide what will we do.

snake = Snake ()

# Moving the snake Automatically.
game_is_on = True
while game_is_on:
    screen.update () # To show the updates happened.
    time.sleep (0.1) # Make it slow.
    snake.move ()   
screen.exitonclick ()

