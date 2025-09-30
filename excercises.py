# Write a dice rolling game program
# Write a python program that keeps asking the user if they want to roll the dice,
# It should ask them to choose a yes/no or y/n as answer.
# If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# tell them 'Invalid choice!' and continue the game.
# If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.

# Steps for Solution
# 1.) Ask the users if they want to roll the dice.
# 2.) If the user enters "Yes" of "Y":
#      generate 2 random dice numbers
# print those numbers.
# 3.) If the user enters "No" of "N":
#      print Gerrout and end game.
# 4.) Else:
# Print invalid choice and input a valid choice and continue with the game.

# --------------- Code -------------

import random

while True:
    user_input = input("Do you want to roll dice? (Yes/No): ")
    if user_input == "Yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1} and {dice2})")
    elif user_input == "No":
        print("Gerrout")
        break
    else:
        print("Invalide choice!!")
