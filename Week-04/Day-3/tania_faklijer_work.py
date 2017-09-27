class Apple(object):

    def get_apple(self):
        return "apple"


class Sum(object):

    def sum(self, list_of_numbers):
        if list_of_numbers == None:
            return None
        else:
            return sum(list_of_numbers)


# class Anagram(object):

#     def anagram(self, list1, list2):
#         compare = list(list1)
#         compare_to = list(list2)
#         if compare.sort() == compare_to.sort():
#             return True 
 