import unittest
import partTwo

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(partTwo.mainFunction(1900), True)

if __name__ == '__main__':
    unittest.main()