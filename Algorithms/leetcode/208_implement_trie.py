class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if not node.children.get(w, None):
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if not node.children.get(w, None):
                return False
            node = node.children[w]
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for p in prefix:
            if not node.children.get(p, None):
                return False
            node = node.children[p]
        return True


        # Your Trie object will be instantiated and called as such:
        # trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")