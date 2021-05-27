import unittest
import partTwo

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(partTwo.mainFunction(1900), False)


class TestCase2(unittest.TestCase):
    def test2(self):
        self.assertEqual(partTwo.mainFunction(2020), True)

class TestCase3(unittest.TestCase):
    def test3(self):
        self.assertEqual(partTwo.mainFunction(2017), False)

class testCase4(unittest.TestCase):
    def test4(self):
        self.assertEqual(partTwo.mainFunction(1220), True)

if __name__ == '__main__':
    unittest.main()

