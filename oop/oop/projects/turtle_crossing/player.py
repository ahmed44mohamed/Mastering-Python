# Importing Section
from turtle import Turtle

# Constant Variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
EDIT_HEAD_OF_THE_TURTLE = 90

class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.shape ("turtle")
        self.penup ()
        self.setheading (EDIT_HEAD_OF_THE_TURTLE)
        self.goto (STARTING_POSITION)
        self.color ("white")
    
    def move_forward (self):
        self.forward (MOVE_DISTANCE)

    def move_back (self):
        self.backward (MOVE_DISTANCE)
    
    def back (self):
        self.goto (STARTING_POSITION)