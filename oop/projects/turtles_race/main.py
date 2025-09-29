from turtle import Turtle, Screen
import random

screen = Screen ()
screen.setup (width= 3000,height= 1500)
user_pit = screen.textinput (title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower ()
colors = ["red", "orange", "black", "green", "blue", "purple"]
all_turtles = []

num = - 400
for color in colors:
    new_turtle = Turtle (shape= "turtle")
    new_turtle.penup ()
    new_turtle.color (color)
    new_turtle.goto (x= - (screen.window_width () - 100) / 2, y= num)
    new_turtle.shapesize (stretch_wid= 3,stretch_len= 3)
    all_turtles.append (new_turtle)
    num += 200

is_race_on = False

if user_pit:
    is_race_on = True


tim = Turtle ()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > (screen.window_width() / 2 - 30):
            is_race_on = False
            winning_color = turtle.pencolor ()
            if winning_color == user_pit:
                print (f"You'have \"won!\" The {winning_color} turtle is the winner!")
            else:
                print (f"You'have \"lost!\" The {winning_color} turtle is the winner!")
        random_distance = random.randint (0, 10)
        turtle.forward (random_distance)


screen.exitonclick ()
