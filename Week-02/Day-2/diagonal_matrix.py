# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

list1 = [[], [], [], []]
for i in range(4):
    list1[i] = [0, 0, 0, 0]
    list1[i][i] += 1
    print (list1[i])