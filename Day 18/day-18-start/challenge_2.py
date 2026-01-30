import turtle as t

mike = t.Turtle()
#draw no draw
for i in range (15):
    mike.fd(10)
    mike.pu()
    mike.fd(10)
    mike.pd()


screen = t.Screen()
screen.exitonclick()

