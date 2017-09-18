# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess.
# If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)

import random

def read_user_parameters():
    user_number = int(input("I've the number between 1-100. You have 5 lives."))
    return user_number

def create_random_numbers():
    random_number = 0
    random_number = random.randint(0,100)
    return random_number

def check_numbers(read_user_parameters, create_random_numbers):
    if read_user_parameters == create_random_numbers:
        return True
        
def user_message():
    if check_numbers == False:
        print("Too low or too high")
    else:
        print("Congratulations. You won!")

user_message()