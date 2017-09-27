class Apple(object):

    def get_apple(self):
        return "apple"


class Sum(object):

    def sum(self, list_of_numbers):
        if list_of_numbers == None:
            return None
        else:
            return sum(list_of_numbers)


class Anagram(object):

    def anagram(self, word1, word2):
        if len(word1) == len(word2):
            if sorted(word1) == sorted(word2):
                return True
        return False


class CountLetters(object):

    def count_letters(self, word):
        number_of_letters = {}
        for letter in word:
            if letter in number_of_letters:
                number_of_letters[letter] += 1
            else:
                number_of_letters[letter] = 1
        return number_of_letters

