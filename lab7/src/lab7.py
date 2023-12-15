def read_from_file(file) -> [int, list[str]]:
    with open(file, "r") as file:
        words_count = file.readline().strip()
        words = [line.strip() for line in file.readlines()]

    return words_count, words


def calculate_maximum_chain(words_count: int, words: list[str]):
    max_chain_lengths = {}
    max_chain_words = {}
    counter = 0

    for word in words:
        if len(word) == 1:
            max_chain_lengths[word] = 1
            max_chain_words[word] = [word]

    for word in words:
        if len(word) > 1:
            max_len = 1
            max_chain = [word]

            for i in range(len(word)):
                counter += 1
                temp_word = word[:i] + word[i + 1:]

                if temp_word in max_chain_lengths:
                    temp_len = max_chain_lengths[temp_word] + 1
                    temp_chain = max_chain_words[temp_word] + [word]

                    if temp_len > max_len:
                        max_len = temp_len
                        max_chain = temp_chain

            max_chain_lengths[word] = max_len
            max_chain_words[word] = max_chain

    max_chain_word = max(max_chain_words.values(), key=len)
    max_chain_length = max(max_chain_lengths.values())
    for zxc in max_chain_words:
        if len(max_chain_words[zxc]) == 7:
            print(max_chain_words[zxc])
    print(counter)
    return max_chain_length, max_chain_word
