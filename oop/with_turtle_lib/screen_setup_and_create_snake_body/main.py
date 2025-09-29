from turtle import Screen, Turtle
# Create object for the screen.
screen = Screen ()
# Setup the screen.
screen.setup (width= 1000, height= 1000)
screen.bgcolor ("black")
screen.title ("My Snake Game")
# Make the body of the turtle by making three turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_turtle = Turtle (shape= "square")
    new_turtle.color ("white")
    new_turtle.goto (position)
# Keep screen on until click on it.
screen.exitonclick ()