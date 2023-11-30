import unittest

from src.third_variant import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.is_word_in_trie("apple"))
        self.assertFalse(self.trie.is_word_in_trie("app"))
        self.assertFalse(self.trie.is_word_in_trie("orange"))

        self.trie.insert("app")
        self.assertTrue(self.trie.is_word_in_trie("app"))
        self.assertTrue(self.trie.is_prefix_in_trie("app"))

    def test_insert_empty_word(self):
        self.assertFalse(self.trie.insert(""))

    def test_is_prefix_in_trie(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.is_prefix_in_trie("app"))
        self.assertFalse(self.trie.is_prefix_in_trie("ore"))

    def test_is_word_in_trie(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.is_word_in_trie("apple"))
        self.assertFalse(self.trie.is_word_in_trie("app"))
        self.assertFalse(self.trie.is_word_in_trie("orange"))


if __name__ == '__main__':
    unittest.main()
