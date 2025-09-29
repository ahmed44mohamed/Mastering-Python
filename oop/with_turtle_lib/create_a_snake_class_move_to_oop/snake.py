from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake ():
    def __init__(self):
        self.turtles = []
        self.create ()

    def create (self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle (shape= "square")
            new_turtle.color ("white")
            new_turtle.penup ()
            new_turtle.goto (position)
            self.turtles.append (new_turtle)

    def move (self):
        for tur_num in range (len (self.turtles) - 1, 0, -1):
            new_x = self.turtles[tur_num - 1].xcor ()
            new_y = self.turtles[tur_num - 1].ycor ()
            self.turtles[tur_num].goto (new_x, new_y)
        self.turtles[0].forward (MOVE_DISTANCE)

