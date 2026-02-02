import turtle as t
import random

mike = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

import turtle as t
import random

list_of_directions = ["forward", "backward", "left", "right"]

mike = t.Turtle()
t.colormode(255)
mike.speed(0)
mike.pensize(2)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        mike.color(random_color())
        mike.circle(100)
        mike.setheading(mike.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
