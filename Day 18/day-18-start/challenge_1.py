from turtle import Turtle, Screen

dartaruga = Turtle()

# draw a square
dartaruga.fd(100)
for i in range(3):
    dartaruga.rt(90)
    dartaruga.fd(100)



screen = Screen()
screen.exitonclick()

