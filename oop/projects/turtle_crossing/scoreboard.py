from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color ("white")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over (self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over.\nLevel: {self.level}", align="center", font=FONT)
