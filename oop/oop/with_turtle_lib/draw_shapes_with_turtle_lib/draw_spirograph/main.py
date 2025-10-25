import random
import turtle


def random_color ():
    r = random.randint (0, 225)
    g = random.randint (0, 225)
    b = random.randint (0, 225)

    return (r, g, b)

turtle.colormode(255)

turtle.speed (0)

def draw_spirograph (size_of_gap):
    for _ in range (int (360 / size_of_gap)):
        turtle.color (random_color ())
        turtle.circle(250)
        turtle.setheading (turtle.heading () + size_of_gap)

draw_spirograph (5)

turtle.Screen ().exitonclick ()