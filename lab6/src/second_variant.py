def compute_lps(pattern: str) -> list[int]:
    # Longest Proper Prefix that is suffix array
    lps = [0] * len(pattern)

    top = 0
    for bottom in range(1, len(pattern)):

        while top and pattern[bottom] != pattern[top]:
            top = lps[top - 1]

        if pattern[top] == pattern[bottom]:
            top += 1
            lps[bottom] = top

    return lps


def kmp(pattern: str, text: str) -> list[int]:
    match_indices = []
    pattern_lps = compute_lps(pattern)

    patterni = 0
    for i, ch in enumerate(text):

        # Phase 3: if a mismatch was found, roll back the pattern
        # index using the information in LPS
        while patterni and pattern[patterni] != ch:
            patterni = pattern_lps[patterni - 1]

        # Phase 2: if match
        if pattern[patterni] == ch:
            # If the end of a pattern is reached, record a result
            # and use infromation in LSP array to shift the index
            if patterni == len(pattern) - 1:
                match_indices.append(i - patterni)
                patterni = pattern_lps[patterni]

            else:
                # Move the pattern index forward
                patterni += 1

        # Phase 1: is implicit here because of the for loop and
        # conditions considered above

    return match_indices


print(kmp("sas", "sasadsadasdassadassasda"))
