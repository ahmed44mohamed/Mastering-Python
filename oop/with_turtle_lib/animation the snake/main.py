# Importing section
import time
from turtle import Screen, Turtle

# Creating object for screen and setup it.
screen = Screen ()
screen.setup (width= 1000, height= 1000)
screen.bgcolor ("black") # Change background color to black.
screen.title ("My Snake Game")
screen.tracer (0) # Hide what will we do.

# Make positions for the squares to make a snake.
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []
for position in starting_positions:
    new_turtle = Turtle (shape= "square")
    new_turtle.color ("white")
    new_turtle.penup ()
    new_turtle.goto (position)
    turtles.append (new_turtle)

# Moving the snake Automatically.
game_is_on = True
while game_is_on:
    screen.update () # To show the updates happened.
    time.sleep (0.1) # Make it slow.
    for tur_num in range (len (turtles) - 1, 0, -1):
        new_x = turtles[tur_num - 1].xcor ()
        new_y = turtles[tur_num - 1].ycor ()
        turtles[tur_num].goto (new_x, new_y)
    turtles[0].forward (20)
    turtles[0].left (90)
screen.exitonclick ()
