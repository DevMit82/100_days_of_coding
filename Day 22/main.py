#TODO wich class we need?
# Classes: Player, Ball, Score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

ball = Ball(x=0,y=0)
paddle_right = Paddle(x = 350,y = 0)
paddle_left = Paddle(x = -350, y = 0)
paddle_left.color("pink")

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

# TODO create Screen
# height = 600, width = 800
# background color
# title

screen.exitonclick()