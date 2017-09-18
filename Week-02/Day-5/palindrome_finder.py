#Create a function named create palindrome following your current language's style guide.
#It should take a string, create a palindrome from it and then return it.
text_number = str(input("Plese enter text or numbers: "))

def palindrome_creator(what_to_palindrome):
    what_to_palindrome += what_to_palindrome[::-1]
    return what_to_palindrome
    print(what_to_palindrome)

palindrome_creator(text_number)