from turtle import Turtle, Screen

screen = Screen ()
tim = Turtle ()
tim.pensize (10)

"""
W --> Forwards
S --> Backwards
C --> clear Drawing

A --> Counter-clockwise
D --> Clockwise
"""

def go_forward ():
    tim.forward (10)

def go_backwards ():
    tim.backward (10)

def clear_screen ():
    tim.clear ()
    tim.penup ()
    tim.home ()
    tim.pendown ()

def clock_wise ():
    new_heading = tim.heading () - 10
    tim.setheading (new_heading)

def counter_clockwise ():
    new_heading = tim.heading () + 10
    tim.setheading (new_heading)

screen.listen ()

screen.onkey (key= "w", fun= go_forward)
screen.onkey (key= "s", fun= go_backwards)
screen.onkey (key= "c", fun= clear_screen)
screen.onkey (key= "d", fun= clock_wise)
screen.onkey (key= "a", fun= counter_clockwise)


screen.exitonclick ()