print(r'''
   *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************                                                                                                                                                                  

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("On the right is a path into the jungle")
print("On the left is an old shipwreck.")

q1 = input("Left or Right\n").lower()

if q1 == "right":
    print("You get lost in the jungle and starve.")
    print("Game Over")
elif q1 == "left":
    print("You find treasure map")
    print("You follow the map come to a beautiful waterfall")
    q2 = input("You want to take shower? Yes or No\n").lower()
    if q2 == "no":
        print("A stone falls on your head.")
        print("Game Over")
    elif q2 == "yes":
        print("You feel refreshed and discover a cave behind the waterfall")
        print("You go into the cave and discover three chests.")
        q3 = input("Which chest you choose? left,middle,right?\n").lower()
        if q3 == "left":
            print("Poison fills the cave and you suffocate.")
            print("Game Over")
        elif q3 == "right":
            print("The chest explodes, and you die.")
            print("Game Over")
        elif q3 == "middle":
            print("All three chests open. They are full of gold.")
            print("You win")
else:
    print("Invalid choice. Game Over")





