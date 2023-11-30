from src.first_variant import find_needle
from src.third_variant import Trie

if __name__ == "__main__":
    trie = Trie()

    words = ["see", "seal", "seen", "saw", "snow", "able", "about", "above", "accept", "account", "across", "act",
             "action", "activity", "add", "address", "afraid", "after", "afternoon", "again", "age", "against", "age",
             "ago", "agree"]

    for word in words:
        trie.insert(word)

    all_prefixes = trie.display_prefixes()
    all_words = trie.display()
    is_word_in_trie = trie.is_word_in_trie("aga:")
    print(is_word_in_trie)
    is_prefix_in_trie = trie.is_prefix_in_trie("app")
    print(is_prefix_in_trie)
