# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect when paddle misses
# Keep score

# Importing section.
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Set up the screen.
screen = Screen ()
screen.setup (width= 1200.0, height= 1000.0)
screen.title ("Pong")
screen.tracer (0)
screen.bgcolor ("black")


# Create two paddles.
r_paddle = Paddle ((560, 0))
l_paddle = Paddle ((-560, 0))


# Create the ball
ball = Ball ()

# Create the scoreboard
scoreboard = ScoreBoard ()


# make paddles move.
screen.listen ()
# Right one
screen.onkey (key= "Up", fun= r_paddle.go_up)
screen.onkey (key= "Down", fun= r_paddle.go_down)
# Left one
screen.onkey (key= "w", fun= l_paddle.go_up)
screen.onkey (key= "s", fun= l_paddle.go_down)


# Keep game going
game_is_on = True

while game_is_on:
    time.sleep (ball.move_speed)
    screen.update ()
    ball.move ()

    # Detect collision with wall
    if ball.ycor () > 500 or ball.ycor () < -500:
        ball.bounce_y ()

    # Detect collision with paddle 
    if ball.distance (r_paddle) < 60 and ball.xcor () > 540 or ball.distance (l_paddle) < 60 and ball.xcor () < -540:
        ball.bounce_x()

    # Detect R paddle misses 
    if ball.xcor () > 580:
        ball.reset_position ()
        ball.bounce_x ()
        scoreboard.l_point ()

    # Detect L paddle misses
    if ball.xcor () < -580:
        ball.reset_position ()
        ball.bounce_x ()
        scoreboard.r_point ()


screen.exitonclick()