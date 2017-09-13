example = "In a dishwasher far far away"

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

example = example[:4] +" galaxy " +example[-12:]
print(example)