from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ----- Screen setup -----
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)   # Turn off automatic animation for manual frame updates

# ----- Game objects -----
scoreboard = Scoreboard()
ball = Ball(x=0,y=0)

# Create paddles on left and right side
paddle_right = Paddle(x = 350,y = 0)
paddle_left = Paddle(x = -350, y = 0)
paddle_left.color("pink")

# ----- Controls -----
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

# ----- Game loop -----
game_is_on = True
while game_is_on:
    screen.update()                 # Refresh screen each frame
    time.sleep(ball.move_speed)     # Control game speed dynamically
    ball.move()                     # Move the ball

    # Detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # Detect collision with left paddle
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Right player missed → left scores
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.add_l_score()

    # Left player missed → right scores
    if ball.xcor() < - 380:
        ball.restart()
        scoreboard.add_r_score()

# Keep window open after game ends
screen.exitonclick()