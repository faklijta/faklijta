# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
a = int(input('add value1'))
b = int(input('add value2'))
c = int(input('add value3'))
d = int(input('add value4'))
e = int(input('add value5'))
sum = a+b+c+d+e
print('Sum:', sum)
avg = (sum/5)
print('Average: ', avg)
