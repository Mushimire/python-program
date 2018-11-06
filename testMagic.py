import unittest
from magicball import *;

class MyTestCase(unittest.TestCase):
    def test_replay(self):
        self.assertEqual(replay(),6)


if __name__ == '__main__':
    unittest.main()
