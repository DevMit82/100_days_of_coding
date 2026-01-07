import random
from art import logo

# List of possible card values
# 11 represents the Ace
cards = [
    11,2,3,4,5,6,7,8,9,10,10,10,10
]

def deal_card():
    """
    Returns a random card from the deck.
    """
    new_card = random.randint(0, 12)
    return cards[new_card]

def calculate_score(cards_list):
    """
    Calculates the score of a hand.
    Returns 0 if the hand is a Blackjack.
    Adjusts Ace value from 11 to 1 if score is over 21.
    """
    score = sum(cards_list)
    # Check for Blackjack
    if score == 21:
        return 0
    # Adjust Ace value if score is too high
    elif 11 in cards_list and score > 21:
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)

    return score

def compare(user_score, computer_score):
    """
    Compares user and computer scores and returns the game result.
    """
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

def blackjack():
    """
    Main function that runs the Blackjack game.
    Handles game flow, user interaction, and replay logic.
    """
    new_game = True

    while new_game:
        # Ask user to start a game
        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
        if start_game == "y":
            # Clear screen effect
            print("\n" * 25)
            # Print Logo
            print(logo)
            game_over = False
            # Initialize card lists
            user_cards = []
            computer_cards = []
            if not game_over:
                    # Deal initial cards
                    user_cards.append(deal_card())
                    user_cards.append(deal_card())

                    computer_cards.append(deal_card())
                    computer_cards.append(deal_card())
                    # Calculate initial scores
                    user_score = calculate_score(user_cards)
                    computer_score = calculate_score(computer_cards)
                    # Display initial hands
                    print(f"    Your cards: {user_cards}, current score: {user_score}" )
                    print(f"    Computer's first card: {computer_cards[0]}")
                    # Check for immediate game end conditions
                    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
                        game_over = True
                    # User decision loop
                    while not game_over:
                        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

                        if another_card == "y":
                            user_cards.append(deal_card())
                            user_score = calculate_score(user_cards)
                            print(f"    Your cards: {user_cards}, current score: {user_score}")
                            print(f"    Computer's first card: {computer_cards[0]}")
                            # End game if user busts or gets Blackjack
                            if user_score == 0 or user_score > 21:
                                game_over = True

                        else:
                            game_over = True
                    # Computer draws cards according to Blackjack rules
                    while computer_score < 17 and user_score != 0 and user_score < 21:
                        computer_cards.append(deal_card())
                        computer_score = calculate_score(computer_cards)

                    # Display final results
                    print(f"    Your final hand {user_cards}, final score: {user_score}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print(compare(user_score, computer_score))

        else:
            # Exit the game loop
            new_game = False

# Start the game
blackjack()


