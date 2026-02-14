from turtle import Turtle

MOVE = 20

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("gold1")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x, y=y)

    def up(self):
        if self.ycor() < 260:
           self.sety(self.ycor() + MOVE)

    def down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - MOVE)







