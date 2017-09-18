# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
import random
random_number = random.randint(0,100)
user_number = int(input("choose a number between 0 and 100: "))
if user_number != random_number:
    if user_number > random_number:
        print('The stored number is lower')
    if user_number < random_number:
        print('The stored number is higher')
if user_number == random_number:
    print("You found the number: "+ random_number)