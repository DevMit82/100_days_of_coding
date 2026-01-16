# TODO Print Logo "Higher Lower"
# import logo
from art import logo
from game_data import data
import random
print(logo)
# TODO Print "Compare A..."
# create a funktion wich gets the data
def create_compare():
   entry = random.choice(data)
   return f"{entry ["name"]}, a {entry ["description"]}, from {entry ["country"]}."
# get needed keys from game_data and put it inside the print statement

compare_a = "Compare A:" + " " + create_compare()
print(compare_a)
#print(f"Compare A: {name}, a {description}, from {country}")
# TODO Print "Vs"
# TODO Print "Against B...."
# TODO ask user for a or b
# TODO print "You 're right + current score
###########################################################
# TODO game logic:
# check if a is higher then b
# check if user answer is right
# give user a score if answer is right
# switch compare b to compare a
# ask next question
# end the game if answer is wrong
