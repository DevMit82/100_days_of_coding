# TODO painting 10 x 10
# TODO dot size = 20
# TODO 50 steps from dot to dot

import turtle as t
import random

# Predefined list of RGB color tuples
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]

# Return a random color from the color list
def random_color():
    new_color = random.choice(color_list)
    return new_color

# Paint a single row of dots
def paint_row(dots_in_row):
    for _ in range(dots_in_row):
        mike.pencolor(random_color())
        mike.fd(50)
        mike.dot(20)

# Move the turtle up and prepare to paint the next row (left turn)
def turn_left():
    mike.lt(90)
    mike.fd(50)
    mike.lt(90)
    mike.pencolor(random_color())
    mike.dot(20)

# Move the turtle up and prepare to paint the next row (right turn)
def turn_right():
    mike.rt(90)
    mike.fd(50)
    mike.rt(90)
    mike.pencolor(random_color())
    mike.dot(20)

mike = t.Turtle()

# Enable RGB color mode
t.colormode(255)

# Lift the pen to avoid drawing lines
mike.penup()
# Move turtle to the starting position for better visualization
mike.goto(200,  -300)

# Paint multiple rows by alternating left and right turns
for _ in range(5):
    turn_left()
    paint_row(9)
    turn_right()
    paint_row(9)

# Keep the window open until the user clicks
screen = t.Screen()
screen.exitonclick()