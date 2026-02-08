from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()

def move_forward():
    mike.fd(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()