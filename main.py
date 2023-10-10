def can_place_cows(free_sections, C, min_distance):
    cows_placed = 1
    last_position = free_sections[0]

    for i in range(1, len(free_sections)):
        if free_sections[i] - last_position >= min_distance:
            cows_placed += 1
            last_position = free_sections[i]

    return cows_placed >= C


def get_max_width(N=9975, C=25, free_sections=[i for i in range(100000)]):
    """
    :param N: count of cows
    :param C: count of aggressive cows
    :param free_sections: free sections
    :return: maximal minimal width
    """
    if N+C > len(free_sections):
        return 0
    elif C == 2:
        return max(free_sections) - min(free_sections)

    free_sections.sort()
    result = 0
    min_distance = 0
    max_distance = free_sections[-1] - free_sections[0]

    while min_distance <= max_distance:
        mid_distance = (min_distance + max_distance) // 2
        if can_place_cows(free_sections, C, mid_distance):
            result = mid_distance
            min_distance = mid_distance + 1
        else:
            max_distance = mid_distance - 1
        print(result)
    return result


if __name__ == '__main__':
    print(get_max_width())
