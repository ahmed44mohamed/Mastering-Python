from turtle import Turtle

class Paddle (Turtle):
    """
    This class for creating the paddles with attributes and methods. 
    """
    def __init__(self, position):
        super().__init__()
        self.goto (position)
        self.shape ("square")
        self.penup ()
        self.color ("white")
        self.shapesize (stretch_len= 1, stretch_wid= 6)
        

    def go_up (self):
        """
        To make the paddle go up 
        """
        new_y = self.ycor () + 50
        self.goto (self.xcor (), new_y)

    def go_down (self):
        """
        To make the paddle go down
        """
        new_y = self.ycor () - 50
        self.goto (self.xcor (), new_y)

