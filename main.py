# def can_place_cows(free_sections, C, min_distance):
#     cows_placed = 1
#     last_position = free_sections[0]
#     print(last_position)
#
#     for i in range(1, len(free_sections)):
#         if free_sections[i] - last_position >= min_distance:
#             print(free_sections[i])
#             cows_placed += 1
#             last_position = free_sections[i]
#
#     return cows_placed >= C
#
#
# def get_max_width(N=10, C=5, free_sections=[1, 2, 3, 4, 5, 10, 30, 40, 60, 90]):
#     """
#     :param N: count of cows
#     :param C: count of aggressive cows
#     :param free_sections: free sections
#     :return: maximal minimal width
#     """
#     if C == 2:
#         return max(free_sections) - min(free_sections)
#
#     free_sections.sort()
#     result = 0
#     min_distance = 0
#     max_distance = free_sections[-1] - free_sections[0]
#
#     while min_distance <= max_distance:
#         mid_distance = (min_distance + max_distance) // 2
#         if can_place_cows(free_sections, C, mid_distance):
#             result = mid_distance
#             min_distance = mid_distance + 1
#         else:
#             max_distance = mid_distance - 1
#     return result

def hamster(S, C, hamsters):
    food_needs = 0
    hamsters.sort(key=lambda x: x[1])
    fed_hamsters = []

    while True:
        for hamster in hamsters:
            food_needs += hamster[0] + hamster[1] * (C - 1)
            fed_hamsters.append(hamster)
        if food_needs <= S:
            return len(fed_hamsters)
        C -= 1
        hamsters.pop()
        food_needs = 0
        fed_hamsters = []


hamsters = [[1, 2],
            [3, 4],
            [5, 6],
            [7, 8]]

print(hamster(10, 4, hamsters))
