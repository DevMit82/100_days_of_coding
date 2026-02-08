import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def make_turtle(name, color, x, y):
    name = t.Turtle(shape="turtle")
    name.color(color)
    name.penup()
    name.goto(x = x, y = y)
    all_turtles.append(name)

make_turtle(name = "mike", color=colors[0], x = -230, y = -100)
make_turtle(name = "leo", color=colors[1], x = -230, y = -60)
make_turtle(name = "don", color=colors[2], x = -230, y = -20)
make_turtle(name = "rafa", color=colors[3], x = -230, y = 20)
make_turtle(name = "giogio", color=colors[4], x = -230, y = 60)
make_turtle(name = "soso", color=colors[5], x = -230, y = 100)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtles is the winner")
            else:
                print(f"You've lost! The {winning_color} turtles is the winner")
        rand_steps = random.randint(0, 10)
        turtle.fd(rand_steps)


screen.exitonclick()
