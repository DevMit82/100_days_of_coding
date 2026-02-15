from turtle import Turtle

# Base movement step of the ball
move = 10

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()                 # Do not draw lines while moving
        self.shape("circle")         # Ball shape
        self.color("white")          # Ball color
        self.goto(x=x,y=y)           # Starting position

        # Direction + speed components for movement physics
        self.x_move = move
        self.y_move = move

        # Controls overall game speed (used in time.sleep)
        self.move_speed = 0.1

    def move(self):
        # Calculate next position based on current direction
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        # Reverse horizontal direction when hitting paddle
        self.x_move *= -1

        # Slightly increase game speed after each paddle hit
        self.move_speed *= 0.9

    def bounce_y(self):
        # Reverse vertical direction when hitting top/bottom wall
        self.y_move *= -1

    def restart(self):
        # Reset ball to center after a score
        self.goto(0, 0)

        # Reset speed to initial value
        self.move_speed = 0.1

        # Send ball toward the opposite player
        self.bounce_x()



