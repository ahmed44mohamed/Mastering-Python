# Importing section
from turtle import Turtle, Screen, colormode
from lists import color_list
from random import choice
# 20 in size and 50 in the spaces between

timmy = Turtle ()
timmy.hideturtle ()
colormode(255)
timmy.speed (0)


def draw_row_with_points (num_point_for_row = 0, num_point_for_col = 0):
    num_increase_spaces_up = 50
    for _ in range (num_point_for_col):
        for _ in range (num_point_for_row):
            timmy.pendown ()
            timmy.dot (20, choice (color_list))
            timmy.penup ()
            timmy.forward (50)
        timmy.goto (0, num_increase_spaces_up)
        num_increase_spaces_up += 50


draw_row_with_points (10, 10)

Screen ().exitonclick ()