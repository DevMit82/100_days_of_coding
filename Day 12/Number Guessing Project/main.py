import random

# TODO import Logo
from art import logo
# TODO print Logo
print(logo)

# TODO list of numbers 1 - 100
numbers_list = []
# adds number between 1 and 100 into number_list
for i in range(1, 101):
    numbers_list.append(i)

# TODO create a random number
right_number = random.choice(numbers_list)

# Variable to loop through the game
game_over = False
# Variable for attempts
attempts = 0

def check_guess(right_number,guess):
    global attempts

    if guess > right_number:
        print("To high")
        print("Guess again")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")

    elif guess < right_number:
        print("To low")
        print("Guess again")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")

# TODO print a welcome message and start the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

# # TODO Ask user for difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# TODO if user chooses easy he gets 10 attempts
if difficulty == "easy":
    attempts += 10
    # TODO print attempts
    print(f"You have {attempts} attempts remaining to guess the number.")

# TODO if user chooses hard he gets 5 attempts
elif difficulty == "hard":
    attempts += 5
    # TODO print attempts
    print(f"You have {attempts} attempts remaining to guess the number.")

# Start the game.
while not game_over:
    # TODO ask user for guess
    guess = int(input("Make a guess: "))
    check_guess(right_number,guess)

    if guess == right_number:
        print (f"You got it! Answer was {right_number}.")
        game_over = True

    elif attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        game_over = True
