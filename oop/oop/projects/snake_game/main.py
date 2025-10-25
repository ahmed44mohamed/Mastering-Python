
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Creating object for screen and setup it.
screen = Screen ()
screen.setup (width= 1500, height= 1500)
screen.bgcolor ("green") # Change background color to green.
screen.title ("Snake Game")
screen.tracer (0) # Hide what will we do.

snake = Snake ()
food = Food ()

scoreboard = ScoreBoard ()

screen.listen()

screen.onkey (fun= snake.up, key= "Up")
screen.onkey (snake.down, key="Down")
screen.onkey (snake.left, key= "Left")
screen.onkey (snake.right, key= "Right")

# Moving the snake Automatically.
game_is_on = True
while game_is_on:
    screen.update ()
    time.sleep (0.1)
    snake.move ()   

    if snake.head.distance (food) < 20:
        print ("nom nom nom 😋")
        food.refresh ()
        snake.extend ()
        scoreboard.increase_score ()

    if snake.head.xcor () > 750 or snake.head.xcor () < -750 or snake.head.ycor () > 750 or snake.head.ycor () < -750:
        scoreboard.reset ()
        snake.reset ()
        print (f"SCORE: {scoreboard.score}")

    for turtle in snake.turtles[1:]:
        if snake.head.distance (turtle) < 10:
            scoreboard.reset ()
            snake.reset ()
            print ("Game Over...!🥲")
            print (f"SCORE: {scoreboard.score}")

screen.exitonclick ()
