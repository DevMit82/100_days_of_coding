# show logo
from art import logo
print(logo)

def get_bids():
    bid = {}
# TODO-1: Ask the user for input
    name = input("What is your name?: ")
#price als int damit wir später die zahlen vergleich können
    price = int(input("Whatis your bid?: "))
# TODO-2: Save data into dictionary {name: price}
    # HIER HEUTE WEITER MACHEN, DICTIONARY RICHTIG ANLEGEN!!
    bid[name] = price
    # TODO-3: Whether if new bids need to be added
    # ask_next = True
    # while ask_next == True:
    #     next_bid = input("Are there any other bidders? Type: 'yes' or 'no'")
    #     if next_bid == "yes":
    #         print("\n" * 100)
    #         bid[name] = input("What is your name?: ")
    #          = int(input("Whatis your bid?: "))
    #         print(bid)
        # else:
        #     ask_next = False
        #     highest_bid = max(bid)
        #     print(max(bid.()))

get_bids()



# TODO-4: Compare bids in dictionary


