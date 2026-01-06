import random

cards = [
    11,2,3,4,5,6,7,8,9,10,10,10,10
]

def deal_card():
    new_card = random.randint(0, 12)
    return cards[new_card]

def calculate_score(cards_list):
    score = sum(cards_list)
    if sum(cards_list) == 21:
        return 0

    elif 11 in cards_list and score > 21:
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)

    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw."
    elif computer_score == 0:
        return "Opponent has a Blackjack! You lose. :-("
    elif user_score == 0:
        return "You have a Blackjack! You win :-)"
    elif user_score > 21:
        return "You went over. You lose :-("
    elif computer_score > 21:
        return "Opponent went over. You win :-)"
    else:
        if computer_score > user_score:
            return "You lose :-("
        else:
            return "You win :-)"



from art import logo
# Ask user to start a game
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
if start_game == "y":
# Print Logo
    print(logo)

user_cards = []
computer_cards = []
game_over = False

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}" )
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
    game_over = True

while not game_over:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or user_score > 21:
            game_over = True

    else:
        game_over = True

while computer_score < 17 and user_score != 0 and user_score < 21:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


print(f"Your final hand {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))


# print cards of the user and current score
# print Computers first card
# ask user for more cards

################################### if yes ###############################################
### print cards of user and current score
### print first card of computer
### if user gets over 21
### print final hand and final score of user
### print final hand and final score of user
### print lose
### ask user for a new game
### if user is not over 21
### ask user for a new card
################################## Case 2a ################################################
### if user says yes

