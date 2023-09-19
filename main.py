def get_longest_peak_subsequence_length(array: list) -> int:
    if len(array) <= 2:
        return 0
    current_subsequence_length = 1
    longest_subsequence_length = 0
    is_reached_peak = False

    for i in range(len(array) - 1):
        if not is_reached_peak:
            if array[i] < array[i + 1]:
                current_subsequence_length += 1
            elif array[i] > array[i + 1] and current_subsequence_length > 1:
                is_reached_peak = True
                current_subsequence_length += 1
        else:
            if array[i] > array[i + 1]:
                current_subsequence_length += 1
            elif array[i] < array[i + 1]:
                longest_subsequence_length = max(longest_subsequence_length, current_subsequence_length)
                current_subsequence_length = 1

    return longest_subsequence_length
