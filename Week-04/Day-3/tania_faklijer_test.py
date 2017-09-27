import unittest
from tania_faklijer_work import Apple

class AppleTestCases(unittest.TestCase):

    def test_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()