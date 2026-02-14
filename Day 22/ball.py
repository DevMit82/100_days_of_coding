from turtle import Turtle

MOVE = 10

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(x=x,y=y)

    def move(self):
        new_x = self.xcor() + MOVE
        new_y = self.ycor() + MOVE
        self.goto(x=new_x, y=new_y)
