# Create a function that takes a number and a list of numbers as a parameter
# Returns the indexes of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
#input = [1, 11, 34, 52, 61], 1

input_list = [1, 11, 34, 52, 61]
input_number = 1

def find_integer(input_list, input_number):
    what_to_find = str(input_number)
    indexes = []
    for i in range(len(input_list)):
        list_index = str(input_list[i])
        if what_to_find in list_index:
            indexes.append(i)
    return indexes
print(find_integer(input_list,input_number))