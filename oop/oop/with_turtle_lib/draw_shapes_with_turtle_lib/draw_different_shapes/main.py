from turtle import Turtle, Screen

import random

timmy = Turtle ()


colors = ["Black", "red", "blue", "green", "orange", "LightPink4", "gray", "brown3"]

def draw_shape (num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        timmy.forward (200)
        timmy.right (angle)

for shape_side_n in range (3, 11):
    timmy.color (random.choice (colors))
    draw_shape (shape_side_n)

# # Triangle
# for _ in range (3):
#     timmy.forward (200)
#     timmy.right (120)


# # Square
# timmy.color ("red")
# for _ in range (4):
#     timmy.forward (200)
#     timmy.right (90)

# # Pentagon
# timmy.color ("blue")
# for _ in range (5):
#     timmy.forward (200)
#     timmy.right (72)


# # Hexagon
# timmy.color ("green")
# for _ in range (6):
#     timmy.forward (200)
#     timmy.right (60)

# # Heptagon
# timmy.color ("orange")
# for _ in range (7):
#     timmy.forward (200)
#     timmy.right (51.428571429)

# # Octagon
# timmy.color ("LightPink4")
# for _ in range (8):
#     timmy.forward (200)
#     timmy.right (45)

# # nonagon
# timmy.color ("gray")
# for _ in range (9):
#     timmy.forward (200)
#     timmy.right (40)

# # decagon
# timmy.color ("brown3")
# for _ in range (10):
#     timmy.forward (200)
#     timmy.right (36)

Screen().exitonclick()