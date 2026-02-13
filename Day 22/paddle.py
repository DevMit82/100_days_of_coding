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
        x = self.xcor()
        y = self.ycor()
        self.goto(x = x, y = y + MOVE)

    def down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x = x, y = y - MOVE)






