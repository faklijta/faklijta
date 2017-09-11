# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have
chicks = int(input('Please add number of chickens: '))
pigs = int(input('Please add the number of pigs: '))
number_of_legs = pigs * 4 + chicks * 2
print(number_of_legs)
