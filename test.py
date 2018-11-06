import unittest
from main import *

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addNumber(2, 5), 7)

    def test_mult(self):
        self.assertEqual(multp(2,2),4)

if __name__ == '__main__':
    unittest.main()
