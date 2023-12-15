import unittest

from src.lab7 import calculate_maximum_chain


class TestCalculateMaximumChain(unittest.TestCase):

    def test_single_word(self):
        words_count = 1
        words = ['apple']
        result = calculate_maximum_chain(words_count, words)
        self.assertEqual(result, 1, f"Expected 1, but got {result}")

    def test_no_chain(self):
        words_count = 3
        words = ['dog', 'cat', 'bat']
        result = calculate_maximum_chain(words_count, words)
        self.assertEqual(result, 1, f"Expected 1, but got {result}")

    def test_simple_chain(self):
        words_count = 4
        words = ['cat', 'bat', 'rat', 'mat']
        result = calculate_maximum_chain(words_count, words)
        self.assertEqual(result, 1, f"Expected 1, but got {result}")

    def test_complex_chain(self):
        words_count = 5
        words = ['apple', 'aple', 'ape', 'ae', 'a']
        result = calculate_maximum_chain(words_count, words)
        self.assertEqual(result, 5, f"Expected 5, but got {result}")

if __name__ == '__main__':
    unittest.main()
