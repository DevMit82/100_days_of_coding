import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
# show logo
from art import logo
print(logo)

def get_bids():
    bids = {}
    more_bidder = True
    while more_bidder is True:
    # TODO-1: Ask the user for input
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        # TODO-2: Save data into dictionary {name: price}
        bids[name] = price
            # TODO-3: Whether if new bids need to be added
        new_bids = input("Are there any other bidders? Type 'yes 'or 'no'").lower()
        if new_bids == "yes":
            clear_screen()
        else:
            more_bidder = False
            # TODO-4: Compare bids in dictionary
            # max()läuft über die Keys
            # key = bids.get sagt: „Vergleiche die Values“
            # Ergebnis ist der Name des Gewinners
            winner = max(bids, key=bids.get)
            # Value von winner abrufen
            highest_bid = bids[winner]
            print(f"The winner is {winner} with a bid of ${highest_bid}")

get_bids()





