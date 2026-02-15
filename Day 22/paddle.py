from turtle import Turtle

# Paddle movement distance per key press
MOVE = 20

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()                         # Prevent drawing lines
        self.color("gold1")                  # Paddle color
        self.shape("square")                 # Base shape
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle tall
        self.goto(x=x, y=y)                  # Set starting position

    def up(self):
        # Move paddle up only if within upper boundary
        if self.ycor() < 260:
           self.sety(self.ycor() + MOVE)

    def down(self):
        # Move paddle down only if within lower boundary
        if self.ycor() > -240:
            self.sety(self.ycor() - MOVE)







