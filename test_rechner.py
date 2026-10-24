import unittest
from rechner import addiere

class TestRechner(unittest.TestCase):
    def test_addiere(self):
        self.assertEqual(addiere(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
