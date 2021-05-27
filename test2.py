import unittest
import test

class TestCase(unittest.TestCase):
    def test1(self):
        finalResults = [1, 2, 'Fizz', 4, 'buzz', 'Fizz', 7, 8, 'Fizz', 'buzz', 11, 'Fizz', 13, 14, 'Fizzbuzz', 16, 17, 'Fizz', 19, 'buzz', 'Fizz', 22, 23, 'Fizz', 'buzz', 26, 'Fizz', 28, 29, 'Fizzbuzz', 31, 32, 'Fizz', 34, 'buzz', 'Fizz', 37, 38, 'Fizz', 'buzz', 41, 'Fizz', 43, 44, 'Fizzbuzz', 46, 47, 'Fizz', 49, 'buzz', 'Fizz', 52, 53, 'Fizz', 'buzz', 56, 'Fizz', 58, 59, 'Fizzbuzz', 61, 62, 'Fizz', 64, 'buzz', 'Fizz', 67, 68, 'Fizz', 'buzz', 71, 'Fizz', 73, 74, 'Fizzbuzz', 76, 77, 'Fizz', 79, 'buzz', 'Fizz', 82, 83, 'Fizz', 'buzz', 86, 'Fizz', 88, 89, 'Fizzbuzz', 91, 92, 'Fizz', 94, 'buzz', 'Fizz', 97, 98, 'Fizz', 'buzz']
        self.assertEqual(test.fizzbuzz(), finalResults)

if __name__ == '__main__':
    unittest.main()
