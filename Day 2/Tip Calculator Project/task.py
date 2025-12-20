print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#calculate the tip
each_person_pay = (bill * (tip/100) + bill) / people

# Print amount per person with 2 decimals
print(f"Each Person should pay ${each_person_pay:.2f}")
