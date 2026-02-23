import turtle

# def get_mouse_click_coor(x, y):
#     print(x, y)


image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
