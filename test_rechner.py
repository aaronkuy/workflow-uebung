import unittest
from rechner import addiere, subtrahiere


class TestRechner(unittest.TestCase):
    def test_addiere(self):
        self.assertEqual(addiere(2, 3), 5)

    def test_subtrahiere(self):
        self.assertEqual(subtrahiere(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
