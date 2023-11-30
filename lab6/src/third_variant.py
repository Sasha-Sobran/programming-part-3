class TrieNode:
    """
    Class for representing the Trie Node
    """

    def __init__(self):
        self.children: dict = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    class for representing the Trie
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        if not word:
            return False
        current_node: TrieNode = self.root
        for char in word:
            current_node.children.setdefault(char, TrieNode())
            current_node = current_node.children.get(char)
        current_node.is_end_of_word = True

    def is_word_in_trie(self, word: str):
        current_node: TrieNode = self.root
        for char in word:
            node: TrieNode = current_node.children.get(char)
            if node:
                current_node = node
            else:
                return False

        if current_node.is_end_of_word:
            return current_node.is_end_of_word

        words = []
        self._display_recursive(current_node, word, words)
        return words

    def is_prefix_in_trie(self, prefix: str):
        current_node: TrieNode = self.root
        for char in prefix:
            node: TrieNode = current_node.children.get(char)
            if node:
                current_node = node
            else:
                return False
        return True

    def display(self):
        words = []
        self._display_recursive(self.root, "", words)
        return words

    def display_prefixes(self):
        prefixes = []
        self._display_prefixes_recursive(self.root, "", prefixes)
        return prefixes

    def _display_recursive(self, node, current_word, words):
        if node.is_end_of_word:
            words.append(current_word)

        for char, child_node in node.children.items():
            self._display_recursive(child_node, current_word + char, words)

    def _display_prefixes_recursive(self, node, current_prefix, prefixes):
        if current_prefix:
            prefixes.append(current_prefix)

        for char, child_node in node.children.items():
            self._display_prefixes_recursive(
                child_node, current_prefix + char, prefixes
            )
