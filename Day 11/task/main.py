import random

cards = [
    11,2,3,4,5,6,7,8,9,10,10,10,10
]

def deal_card():
    new_card = random.randint(-4, 0)
    return cards[new_card]

def calculate_score(cards_list):
    score = sum(cards_list)
    if sum(cards_list) == 21:
        return 0
    return score


from art import logo
# Ask user to start a game
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
if start_game == "y":
# Print Logo
    print(logo)
user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
user_score = calculate_score(user_cards)
computer_cards.append(deal_card())
computer_cards.append(deal_card())
print(f"Your cards: {user_cards}, current score: {user_score}" )
print(computer_cards[0])


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

