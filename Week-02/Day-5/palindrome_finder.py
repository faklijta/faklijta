#Create a function named create palindrome following your current language's style guide.
#It should take a string, create a palindrome from it and then return it.
user_input = list(input("Enter a word or phrase: "))

def create_palindrome(phrase):
    palindrome = []
    for char in range(len(phrase)):
        palindrome.append(phrase[-char-1])
    palindrome = phrase + palindrome
    print("".join(palindrome))

create_palindrome(user_input)