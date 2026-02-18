from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()                  # No drawing lines
        self.color("DeepPink")        # Score text color
        self.speed("fastest")         # Instant drawing
        self.ht()                     # Hide turtle cursor
        self.lvl = 0                  # Current level
        self.update_lvl()             # Draw initial level

    def update_lvl(self):
        # Display the current level in top-left corner
        self.goto(x=-280, y=250)
        self.write(f"Level: {self.lvl}", align="left", font=(FONT))

    def add_lvl(self):
        # Increase level and refresh display
        self.clear()
        self.lvl +=1
        self.update_lvl()

    def game_over(self):
        # Show Game Over message in center
        self.goto(0, 0)
        self.color("black")
        self.write("!!!Game!Over!!!", align = "center", font =(FONT))
