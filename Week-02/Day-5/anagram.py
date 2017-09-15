#Create a function named is anagram following your current language's style guide. 
#It should take two strings and return a boolean value depending on whether its an anagram or not.
phrase1 = "I love python"
phrase2 = "Envy ho pilot"


def anagram(list1,list2):
    compare = list(list1)
    compare_to = list(list2)
    return compare.sort() == compare_to.sort()
    print("You found an anagram")


anagram(phrase1,phrase2)