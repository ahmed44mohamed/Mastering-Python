# OOP --> Object Oriented Programming

# We think about two thing:
# what date it has: attributes
# what date it does: methods

from turtle import Turtle, Screen

timmy = Turtle () # object_name = ClassName ()

print (timmy)

timmy.shape ("turtle") # Change the shape

timmy.color ("green") # Change the color

timmy.forward (100) # Move

Screen ().canvheight = 400 # Change height = 400

print (Screen ().canvheight)

Screen ().exitonclick ()
