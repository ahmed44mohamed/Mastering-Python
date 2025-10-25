from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake ():
    def __init__(self):
        self.turtles = []
        self.create ()
        self.head = self.turtles[0]

    def create (self):
        for position in STARTING_POSITIONS:
            self.add_turtle (position)

    def add_turtle (self, position):
            new_turtle = Turtle (shape= "square")
            new_turtle.color ("white")
            new_turtle.penup ()
            new_turtle.goto (position)
            self.turtles.append (new_turtle)

    def extend (self):
        self.add_turtle (self.turtles[-1].position ())

    def move (self):
        for tur_num in range (len (self.turtles) - 1, 0, -1):
            new_x = self.turtles[tur_num - 1].xcor ()
            new_y = self.turtles[tur_num - 1].ycor ()
            self.turtles[tur_num].goto (new_x, new_y)
        self.head.forward (MOVE_DISTANCE)
    
    def up (self):
        if self.head.heading () != DOWN:
            self.head.setheading (UP)

    def down (self):
        if self.head.heading () != UP:
                self.head.setheading (DOWN)

    def left (self):
        if self.head.heading () != RIGHT:
            self.head.setheading (LEFT)

    def right (self):
        if self.head.heading () != LEFT:
            self.head.setheading (RIGHT)

    def reset (self):
        for tur in self.turtles:
            tur.goto (2000, 2000)
        self.turtles.clear ()
        self.create ()
        self.head = self.turtles[0]