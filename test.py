import unittest

from main import get_max_width


class GetMaxWidthTest(unittest.TestCase):

    def test(self):
        self.assertEqual(get_max_width(5, 3, [1, 2, 8, 4, 9]), 3)


if __name__ == "__main__":
    unittest.main()
