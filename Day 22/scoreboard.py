from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()                  # Prevent drawing lines while moving
        self.color("DeepPink")        # Set text color for the score display
        self.speed("fastest")         # Draw instantly without animation delay
        self.ht()                     # Hide the turtle cursor
        self.goto(x=-100, y=200)      # Initial position (left score area)

        # Initialize score values
        self.l_score = 0
        self.r_score = 0

        # Draw the initial score on screen
        self.update_score()


    def update_score(self):
        # Write left player's score
        self.goto(x=-100, y=200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))

        # Write right player's score
        self.goto(x=100, y=200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def add_l_score(self):
        # Clear previous score display
        self.clear()

        # Increase left player's score
        self.l_score += 1

        # Redraw updated score
        self.update_score()


    def add_r_score(self):
        # Clear previous score display
        self.clear()

        # Increase right player's score
        self.r_score += 1

        # Redraw updated score
        self.update_score()



