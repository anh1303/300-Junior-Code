class Trie(object):
    
    class TrieNode(object):
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = self.TrieNode()
            current = current.children[char]
        current.is_end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end == True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)