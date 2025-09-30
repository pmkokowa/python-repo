# # Write a dice rolling game program
# # Write a python program that keeps asking the user if they want to roll the dice,
# # It should ask them to choose a yes/no or y/n as answer.
# # If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# # If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# # tell them 'Invalid choice!' and continue the game.
# # If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.

# # Steps for Solution
# # 1.) Ask the users if they want to roll the dice.
# # 2.) If the user enters "Yes" of "Y":
# #      generate 2 random dice numbers
# # print those numbers.
# # 3.) If the user enters "No" of "N":
# #      print Gerrout and end game.
# # 4.) Else:
# # Print invalid choice and input a valid choice and continue with the game.

# # --------------- Code -------------

# import random

# while True:
#     user_input = input("Do you want to roll dice? (yes/no): ").lower().strip()
#     if user_input == "yes":
#         dice1 = random.randint(1, 6)
# #         dice2 = random.randint(1, 6)
# #         print(f"({dice1} and {dice2})")
# #     elif user_input == "no":
# #         print("Gerrout")
# #         break
# #     else:
# #         print("Invalide choice!!")


# # -------------- REVERSE A STRING ---------------------
# # user_input = input("input anything please:  ")
# # reversed_input = user_input[::-1]
# # print("reversed input is:", reversed_input)

# # ------------- REVERSE A GROUP OF WORDS ------------------

# import qrcode
# statement = "Lunch break will soon be over"
# words = statement.split()
# reversed_words = words[::-1]
# reversed_statement = " ".join(reversed_words)
# print(reversed_statement)


# # ------------- REVERSE A GROUP OF WORDS ------------------ 2

# def reverse_words():
#     sentence = input("Enter a group of words: ")
#     words = sentence.split()
#     reversed_words = ' '.join(reversed(words))
#     print("Reversed words:", reversed_words)


# reverse_words()


# ---- Write a a python program that takes a URL and generate
# a QR Code for the given URL and save QR Code in a file ----


import qrcode

data = input("Enter your URL: ")
filename = input("Enter your prefered filename: ")
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")

image.save(filename)
print(f"QR Code saved as {filename}")
