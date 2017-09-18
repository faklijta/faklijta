# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
nol = int(input('please add a number: '))
def drawer():
    for i in range(1,nol+1):
        print(" "*(nol-i)+"*"*(i*2-1))
drawer()