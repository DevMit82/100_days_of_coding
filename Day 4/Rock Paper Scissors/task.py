#Schere-Stein-Papier

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Liste und Variable für Computerwahl
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Variable für Userwahl, Eingabe zu int umwandeln um Index in der Liste auwählen zu können
user_input = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors\n"))

# sicherstellen, dass userinput zwischen 0 und 2 liegt um korrekt auf die liste
# choices zugreifen zu können, wenn nicht Fehlermeldung ausgeben
#Zugehörife ASCI Grafiken ausgeben
if 0 <= user_input < len(choices):
    user_choice = choices[user_input]
    if user_choice == 'rock':
        print(rock)
    elif user_choice == 'paper':
        print(paper)
    elif user_choice == 'scissors':
        print(scissors)
    if computer_choice == 'rock':
            print("Computer choose:")
            print(rock)
    elif computer_choice == 'paper':
            print("Computer choose:")
            print(paper)
    else:
            print("Computer choose:")
            print(scissors)
else:
    print("Invalid input, you lose")
#########################################################################################################
                                    #Spiellogig
#Spieler gewinnt ausgeben wenn:
#Spieler hat stone und Computer hat scissors
#oder wenn Spieler paper und Computer rock
#oder wenn Spieler scissors hat und Computer paper
#Unentschieden ausgeben wenn:
# user_choice gleich computer_choice
# in allen anderen Fällen:
# Computer gewinnt ausgeben
########################################################################################################
if (
    (user_choice == 'rock' and computer_choice == 'scissors')
    or (user_choice == 'paper' and computer_choice == 'rock')
    or (user_choice == 'scissors' and computer_choice == 'paper')
):
    print("You win!")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("Computer wins!")








