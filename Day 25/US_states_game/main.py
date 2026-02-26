from turtle import Turtle, Screen
import pandas

# def get_mouse_click_coor(x, y):
#     print(x, y)

writing_t = Turtle()
writing_t.ht()
picture_t = Turtle()

image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
picture_t.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

STATES = 50
score = 0
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while score < STATES:
    if answer_state == "Exit":
        break
    elif answer_state in state_list:
        row = data[data.state == answer_state]
        x_cor = int(row.x.iloc[0])
        y_cor = int(row.y.iloc[0])
        writing_t.teleport(x= x_cor, y= y_cor)
        writing_t.write(answer_state, align="center", font=("Arial", 8, "bold"))
        score += 1
        state_list.remove(answer_state)
        answer_state = screen.textinput(title=f"{score}/{STATES} States Correct",
                                        prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{score}/{STATES} States Correct",
                                        prompt="What's another state's name?").title()

data = pandas.DataFrame(state_list)
data.to_csv("states_to_learn.csv")