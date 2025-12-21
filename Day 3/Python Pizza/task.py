

bill = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25

if pepperoni == "Y" or pepperoni == "y":
    if size == "s" or size == "S":
        bill += 2
    elif size == "m" or size == "M":
        bill += 3
    elif size == "L" or size == "l":
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
print (f"Your final bill is: ${bill}.")