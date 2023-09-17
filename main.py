import unittest


def get_longest_subsequence_len(array: list) -> int:
    if array.__len__() <= 2:
        return 0
    current_subsequence_len = 1
    longest_subsequence_len = 0
    is_reached_peak = False

    for i in range(array.__len__() - 1):
        if not is_reached_peak:
            if array[i] < array[i + 1]:
                current_subsequence_len += 1
            elif array[i] > array[i + 1] and current_subsequence_len > 1:
                is_reached_peak = True
                current_subsequence_len += 1
        elif is_reached_peak:
            if array[i] > array[i + 1]:
                current_subsequence_len += 1
            elif array[i] < array[i + 1] or array[i + 1] is None:
                longest_subsequence_len = max(longest_subsequence_len, current_subsequence_len)
                current_subsequence_len = 1

    return longest_subsequence_len


class TestGetLongestSubsequenceLen(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(get_longest_subsequence_len([1, 2, 3, 4, 5]), 0)

    def test_reverse_sorted_array(self):
        self.assertEqual(get_longest_subsequence_len([5, 4, 3, 2, 1]), 0)

    def test_two_element_array(self):
        self.assertEqual(get_longest_subsequence_len([1, 2]), 0)

    def test_no_peak_subsequence(self):
        self.assertEqual(get_longest_subsequence_len([-1, - 5, - 1]), 0)

    def test_three_peak_subsequence(self):
        self.assertEqual(
            get_longest_subsequence_len([1, 3, 5, 4, 2, 8, 3, 7, 1, 3, 5, 4, 2, 8, 3, 7, 1, 3, 5, 4, 2, 8, 3, 7, ]), 5)


if __name__ == "__main__":
    unittest.main()
