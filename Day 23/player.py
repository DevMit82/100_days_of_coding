from turtle import Turtle

# Player starting position
STARTING_POSITION = (0, -280)

# Movement step per key press
MOVE_DISTANCE = 10

# Finish line position
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()           # Prevent drawing
        self.shape("turtle")   # Turtle player shape
        self.restart()         # Move to starting position
        self.seth(90)          # Face upward

    def move(self):
       # Move player forward (up)
       self.fd(MOVE_DISTANCE)

    def restart(self):
        # Reset player to starting position after reaching finish
        self.goto(x=0, y=-300)
