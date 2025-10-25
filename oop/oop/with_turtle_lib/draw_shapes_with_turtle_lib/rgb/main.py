import random
import turtle
from lists import directions

turtle.colormode(255)

tim = turtle.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.pensize(20)
tim.speed(20)

for _ in range(200):
    tim.setheading(random.choice(directions))
    tim.forward(30)
    tim.color(random_color())

turtle.Screen().exitonclick()
