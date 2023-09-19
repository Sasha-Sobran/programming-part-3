import unittest

from main import get_longest_subsequence_length


class TestGetLongestSubsequenceLen(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(get_longest_subsequence_length([1, 2, 3, 4, 5]), 0)

    def test_reverse_sorted_array(self):
        self.assertEqual(get_longest_subsequence_length([5, 4, 3, 2, 1]), 0)

    def test_two_element_array(self):
        self.assertEqual(get_longest_subsequence_length([1, 2]), 0)

    def test_no_peak_subsequence(self):
        self.assertEqual(get_longest_subsequence_length([-1, - 5, - 1]), 0)

    def test_three_peak_subsequence(self):
        self.assertEqual(
            get_longest_subsequence_length([1, 3, 5, 4, 2, 8, 3, 7, 1, 3, 4, 2, 8, 3, 7, 1, 5, 4, 8, 3, 7, ]), 5)


if __name__ == "__main__":
    unittest.main()
