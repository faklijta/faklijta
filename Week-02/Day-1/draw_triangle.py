# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number_of_lines = int(input("Please add number of lines: "))

def triangle():
    for lines in range(1, number_of_lines+1):
            print("*" * lines)

triangle()