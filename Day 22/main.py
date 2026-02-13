#TODO wich class we need?
# Classes: Player, Ball, Score
from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

paddle_right = Paddle(350, 0)

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)



# TODO create Screen
# height = 600, width = 800
# background color
# title

screen.exitonclick()