# Import ASCII art and comparison graphic
from art import logo, vs
# Import game data (list of dictionaries)
from game_data import data
import random

def create_compare():
    """
    Selects and returns two different random entries from the game data.
    Each entry is a dictionary containing name, description, country,
    and follower_count.
    """
    entry_1 = random.choice(data)
    entry_2 = random.choice(data)
    # Ensure both entries are not the same
    while entry_2 == entry_1:
        entry_2 = random.choice(data)
    return entry_1, entry_2

# Print game logo at start
print(logo)

# Initialize score
score = 0

# Get initial comparison entries
compare_a, compare_b = create_compare()

# Game loop control flag
game_over = False
while not game_over:
    # Display first comparison entry
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']},from {compare_a['country']}.")

    # Display versus graphi
    print(vs)

    # Display second comparison entry
    print(f"Against B: {compare_b['name']}, a {compare_b['description']},from {compare_b['country']}.")

    # Ask user for a or b
    answer = input("Type 'A' or 'B': ").lower()

    # Case: User chooses A and A has more followers
    if answer == "a" and compare_a["follower_count"] > compare_b["follower_count"]:
        score += 1
        print(logo)
        print(f"You are right! Current score: {score}")
        # Move B to A and generate a new B
        compare_a = compare_b
        compare_b, _ = create_compare()

        # Ensure new B is not the same as A
        while compare_b == compare_a:
            compare_b, _ = create_compare()

    # Case: User chooses B and B has more followers
    elif answer == "b" and compare_b["follower_count"] > compare_a["follower_count"]:
        score += 1
        print(logo)
        print(f"You are right! Current score: {score}")
        compare_a = compare_b
        compare_b, _ = create_compare()
        while compare_b == compare_a:
            compare_b, _ = create_compare()

    # Case: User is wrong
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

