# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
nol = int(input('please add a number: '))
def drawer():
    for i in range(1,nol+1):
        if i == 1 or i== nol:
            print("%"*(nol-1))
        else:
            print("%"+" "*(nol-3)+"%")
drawer()