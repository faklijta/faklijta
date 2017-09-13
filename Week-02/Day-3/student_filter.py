students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies
def candies_above4():
    for i in range(len(students)):
        if students[i]['candies'] > 4:
            print (students[i]['name'])
candies_above4()
# create a function that takes a list of students and prints: 
#  - how many candies they have on average
def candies_avg():
    sum_candies = 0
    for i in range(len(students)):
        sum_candies += students[i]['candies']
        avg_candies = sum_candies/(len(students))
    print(str(avg_candies))

        #print(sum_candies)
candies_avg()