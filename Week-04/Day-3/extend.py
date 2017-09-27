import statistics

# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
    if c > a:
        if c > b:
            return c
    if b > a:
        if b > c:
            return b

# Returns the median value of a list given as param
def median(pool):
    return statistics.median(pool)

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóíú'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in set(teve):
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve