# Importing section
from turtle import Turtle, Screen
from random import choice
from lists import directions, colors

# Make an object form Turtle class
timmy = Turtle ()


timmy.pensize (20)
timmy.speed (20)

for _ in range (200):
    timmy.forward (30)
    timmy.setheading (choice (directions))
    timmy.color (choice (colors))

Screen ().exitonclick ()