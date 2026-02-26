from turtle import Turtle, Screen
import pandas
import os

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

with open("highscore", "r") as f:
    highscore = f.read()


player_name = screen.textinput(title="Guess the State", prompt="Please, enter your name!").title()
if os.path.exists(f"states_to_learn_{player_name}.csv"):
    os.remove(f"states_to_learn_{player_name}.csv")
answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()


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
data.to_csv(f"states_to_learn_{player_name}.csv")

new_score = STATES - len(data)
with open("highscore", "r") as f:
    line = f.readline().strip()
    parts = line.split(",")
    player = parts[0]
    highscore = int(parts[1])


if new_score > int(highscore):
    with open("highscore", "w") as f:
        highscore = new_score
        f.write(f"{player_name},{str(highscore)}")
        print(f"Congratulations {player_name}!!! New Highscore!! You guessed {highscore} states correct.")

elif player_name == player and new_score < highscore:
    print(f"You guessed {new_score} states correct. "
          f"No Highscore, but you are still the Best, {player_name}!")

else:
    print(f"You guessed {new_score} states correct. {player} guessed {int(highscore) - new_score} "
          f"more than you {player_name}...")