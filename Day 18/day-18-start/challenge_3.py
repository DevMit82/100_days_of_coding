import turtle as t
import random

list_of_colors= ["red", "blue", "green", "yellow", "orange",
                 "brown", "gold1", "magenta", "gray0", "hotpink"
]

mike = t.Turtle()

# mike.color(random.choice(list_of_colors))
# #draw a triangle
# for i in range(3):
#     mike.rt(120)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# #draw a square
# for i in range(4):
#     mike.rt(90)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# #draw a pentagon
# angle = 360 / 5
# for i in range(5):
#     mike.rt(angle)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# #draw a hexagon
# angle = 360 / 6
# for i in range(6):
#     mike.rt(angle)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# #draw a heptagon
# angle = 360 / 7
# for i in range(7):
#     mike.rt(angle)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# # drar a octagon
# angle = 360 / 8
# for i in range(8):
#     mike.rt(angle)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# # draw a nonagon
# angle = 360 / 9
# for i in range(9):
#     mike.rt(angle)
#     mike.fd(100)
#
# mike.color(random.choice(list_of_colors))
# #draq a decagon
# angle = 360 / 10
# for i in range(10):
#     mike.rt(angle)
#     mike.fd(100)

def draw_shape(sides):
    for i in range(sides):
        angle = 360 / sides
        mike.rt(angle)
        mike.fd(100)

for drawing in range (3, 11):
    draw_shape(drawing)
    mike.color(random.choice(list_of_colors))

screen = t.Screen()
screen.exitonclick()