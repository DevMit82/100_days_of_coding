from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15,"bold")
FONT_GAME_OVER = ("Courier", 20,"bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("DeepPink")
        self.speed("fastest")
        self.ht()
        self.goto(x=0, y=280)
        self.score = 0
        self.write(arg = f"Score: {self.score}",align=ALIGNMENT, font=FONT )


    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg = f"Score: {self.score}",align=ALIGNMENT , font=FONT )

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("firebrick1")
        self.write(arg=f"!!!GAME!OVER!!!", align=ALIGNMENT, font=FONT_GAME_OVER)
