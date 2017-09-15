#Write a simple program to check if a given number is an armstrong number. 
# The program should ask for a number. E.g. if we type 371, the program should print out: 
# The 371 is an Armstrong number.

user_input = input("Please type in the number:")

def armsrtong_no(input): 

    power = len(input)
    result = 0

    for i in range(len(input)):
        result += int(input[i]) ** power
    
    if result == int(input):
        print("The " + user_input + " is an Armstrong number")
armsrtong_no(user_input)
