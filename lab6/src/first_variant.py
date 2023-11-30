def find_needle(haystack, needle):
    if not needle:
        return []

    needle_length, haystack_length = len(needle), len(haystack)
    transitions = compute_transition_function(needle)

    indices = []
    state = 0
    for i in range(haystack_length):
        while state > 0 and haystack[i] != needle[state]:
            state = transitions[state - 1]
        if haystack[i] == needle[state]:
            state += 1
        if state == needle_length:
            indices.append(i - needle_length + 1)
            state = transitions[state - 1]
    return indices


def compute_transition_function(needle):
    m = len(needle)
    transitions = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and needle[k] != needle[q]:
            k = transitions[k - 1]

        if needle[k] == needle[q]:
            k += 1
        print(transitions)
        transitions[q] = k
    return transitions
