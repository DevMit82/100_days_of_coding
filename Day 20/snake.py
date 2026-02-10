from turtle import Turtle

class Snake:
    def __init__(self):
        self.squares = []
        self.create_square(x=0, y=0)
        self.create_square(-20, 0)
        self.create_square(-40, 0)

    def create_square(self, x, y):
        square = Turtle(shape="square")
        square .penup()
        square .color("white")
        square .setpos(x=x, y=y)
        self.squares.append(square)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].fd(20)




