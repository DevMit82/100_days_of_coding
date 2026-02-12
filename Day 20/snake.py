from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.create_square(x=0, y=0)
        self.create_square(-20, 0)
        self.create_square(-40, 0)
        # self.up()
        # self.down()
        # self.left()
        # self.right()

    def create_square(self, x, y):
        square = Turtle(shape="square")
        square.penup()
        square.color("HotPink")
        square.setpos(x=x, y=y)
        self.squares.append(square)

    def extend(self):
        last_square = self.squares[-1]
        x = last_square.xcor()
        y = last_square.ycor()
        self.create_square(x, y)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].seth(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].seth(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].seth(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].seth(RIGHT)


