def read_from_file(file) -> [int, list[str]]:
    with open(file, "r") as file:
        words_count = file.readline().strip()
        words = [line.strip() for line in file.readlines()]

    return words_count, words


def calculate_maximum_chain(words_count: int, words: list[str]):
    max_chain_lengths = {}

    def max_chain_length(word):
        if word in max_chain_lengths:
            return max_chain_lengths[word]

        if len(word) == 1:
            return 1

        max_len = 1

        for i in range(len(word)):
            temp_word = word[:i] + word[i + 1:]
            if temp_word in words:
                temp_len = 1 + max_chain_length(temp_word)
                max_len = max(max_len, temp_len)

        max_chain_lengths[word] = max_len
        return max_len

    max_chain = max(max_chain_length(word) for word in words)

    return max_chain
