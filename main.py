def get_longest_peak_subsequence_length(array: list) -> int:
    if len(array) <= 2 or array == selection_sort(array.copy()):
        return 0

    current_subsequence_length = 1
    longest_subsequence_length = 0
    current_array = [array[0]]
    max_array = []
    is_reached_peak = False

    for i in range(len(array) - 1):
        if array[i] > array[i + 1] and is_reached_peak:
            current_array = [array[i + 1]]
            continue
        if not is_reached_peak:
            if array[i] < array[i + 1]:
                current_array.append(array[i + 1])
                current_subsequence_length += 1
            elif array[i] > array[i + 1] and current_subsequence_length > 1:
                is_reached_peak = True
                current_array.append(array[i + 1])
                current_subsequence_length += 1
        else:
            if array[i] > array[i + 1]:
                current_subsequence_length += 1
                current_array.append(array[i + 1])

            if array[i] < array[i + 1]:
                current_subsequence_length = 2
                current_array = [array[i], array[i + 1]]
                is_reached_peak = False

        longest_subsequence_length = max(longest_subsequence_length, current_subsequence_length)
        if len(current_array) > len(max_array):
            max_array = current_array.copy()

    if longest_subsequence_length >= 3:
        print(max_array)
        return longest_subsequence_length

    return 0


def selection_sort(array):
    sorted_array = []
    length = len(array)
    count = 0
    for i in range(length):
        min_index = i
        count += 1
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
            count +=1
        array[i], array[min_index] = array[min_index], array[i]

        sorted_array.append(array[i])
    return sorted_array

if __name__ == "__main__":
    my_array1 = [1, 3, 5, 4, 8, 3, 7]
    my_array2 = [1, 3, 8, 9, 10, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 0]
    my_array3 = [1, 2, 1, 2, 3, 4, 2]
    my_array4 = [1, 2, 1]
    my_array5 = [-1, -2, -1]
    my_array6 = [1, 2, 3, 4, 5]
    my_array7 = [5, 4, 3, 2, 1]
    my_array8 = [1, 2]
    my_array9 = [1, 1, 1, 1, 1]
    my_array10 = [-1, -1, 0, 1, 2, -1]
    print(get_longest_peak_subsequence_length(my_array1))
    print(get_longest_peak_subsequence_length(my_array2))
    print(get_longest_peak_subsequence_length(my_array3))
    print(get_longest_peak_subsequence_length(my_array4))
    print(get_longest_peak_subsequence_length(my_array5))
    print(get_longest_peak_subsequence_length(my_array6))
    print(get_longest_peak_subsequence_length(my_array7))
    print(get_longest_peak_subsequence_length(my_array8))
    print(get_longest_peak_subsequence_length(my_array9))
    print(get_longest_peak_subsequence_length(my_array10))
