# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
number = int(input("please add a number"))

def divide(number):
    try:
        calculation = 10 / number
        print(calculation)
    except ZeroDivisionError:
        print("fail")
divide(number)

