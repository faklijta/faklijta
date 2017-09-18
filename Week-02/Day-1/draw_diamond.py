# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

nol = int(input('please add a number: '))
def drawer():
    for i in range(1,(nol+1)//2+1):
        print(" "*((nol+1)//2-i)+"*"*(i*2-1))
    if nol%2 != 0:   
        for i in range(1,nol//2+1):
            print(" "*i+"*"*(nol-i*2))
    else:   
        for i in range(1,nol//2+1):
            print(" "*(i-1)+"*"*((nol+1)-i*2))
drawer()