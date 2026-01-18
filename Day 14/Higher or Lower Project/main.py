# TODO Print Logo "Higher Lower"
# import logo
from art import logo, vs
from game_data import data
import random
print(logo)
# TODO Print "Compare A..."
# create a funktion wich gets the data
def create_compare():

    # get 2 different random entry from game_data
    entry_1 = random.choice(data)
    entry_2 = random.choice(data)
    while entry_2 == entry_1:
        entry_2 = random.choice(data)
    return entry_1, entry_2

score = 0
compare_a, compare_b = create_compare()
game_over = False
while not game_over:
    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]},from {compare_a["country"]}.")

    # # TODO Print "Vs"
    print(vs)
    # # TODO Print "Against B...."
    print(f"Against B: {compare_b["name"]}, a {compare_b["description"]},from {compare_b["country"]}.")
    # TODO ask user for a or b
    answer = input("Type 'A' or 'B': ").lower()
    if answer == "a" and compare_a["follower_count"] > compare_b["follower_count"]:
        score += 1
        print(logo)
        print(f"You are right! Current score: {score}")
        compare_a = compare_b
        compare_b, _ = create_compare()
    elif answer == "b" and compare_b["follower_count"] > compare_a["follower_count"]:
        score += 1
        print(logo)
        print(f"You are right! Current score: {score}")
        compare_a = compare_b
        compare_b, _ = create_compare()
    else:
        print("\n"* 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True


# TODO print "You 're right + current score
###########################################################
# TODO game logic:
# check if follower of a is higher then follower of b
# check if user answer is right
# give user a score if answer is right
# switch compare b to compare a
# ask next question
# end the game if answer is wrong

