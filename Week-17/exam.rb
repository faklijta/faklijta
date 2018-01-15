# Create a function that takes a list of numbers and returns
# a new list where all the duplicate values are removed

# array built in method

def duplicate_remover(num_list)
  num_list.uniq
end

list_of_numbers = [1, 2, 3, 3, 5, 2]

print(duplicate_remover(list_of_numbers))

# with looping

def duplicate_remover2(numbers)
  new_list = []
  numbers.each do |e|
    new_list << e unless new_list.include?(e)
  end
  print(new_list)
end

list_of_numbers = [1, 2, 3, 3, 5, 2]

duplicate_remover2(list_of_numbers)
