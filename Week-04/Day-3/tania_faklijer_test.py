import unittest
from tania_faklijer_work import Apple
from tania_faklijer_work import Sum, Anagram, CountLetters

class AppleTestCases(unittest.TestCase):

    def test_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

class SumTestCases(unittest.TestCase):

    def test_sum(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1, 2, 3]), 6)

    def test_sum_if_empty(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([]), 0)

    def test_if_one_element(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1]), 1)

    def test_if_multiple_element(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1, 2, 3, 4, 5]), 15)

    def test_if_null(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum(None), None)       

class AnagramTestCase(unittest.TestCase):

    def test_anagram(self):
        test_anagram = Anagram()
        self.assertTrue(test_anagram.anagram('alma', 'lama'))

    def test_if_not_anagram(self):
        test_anagram = Anagram()
        self.assertFalse(test_anagram.anagram('apa', 'app'))

class CountLettersTestCase(unittest.TestCase):

    def test_if_empty(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters(""), {})
    
    def test_if_one(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters('kacsa')['k'] , 1)

    def test_if_two(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters('kacsa')['a'] , 2)



if __name__ == '__main__':
    unittest.main()