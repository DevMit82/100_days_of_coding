import turtle as t
import random

list_of_directions = ["forward", "backward", "left", "right"]

mike = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

def random_walk(num_of_steps):
    steps = 0
    mike.speed(10)
    mike.pensize(10)
    while steps <= num_of_steps:
        direction = random.choice(list_of_directions)
        if direction == "forward":
            mike.color(random_color())
            mike.fd(20)
            steps += 1
        elif direction == "backward":
            mike.color(random_color())
            mike.bk(20)
            steps += 1
        elif direction == "left":
            mike.color(random_color())
            mike.lt(90)
        elif direction == "right":
            mike.color(random_color())
            mike.rt(90)

random_walk(200)

screen = t.Screen()
screen.exitonclick()