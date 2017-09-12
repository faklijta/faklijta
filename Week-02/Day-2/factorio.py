# - Create a function called `factorio`
#   that returns it's input's factorial
#numbers = int(input ("please add a number"))
numbers = 4
def factorio(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(factorio(numbers))
        