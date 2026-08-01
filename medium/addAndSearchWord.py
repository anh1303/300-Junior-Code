class WordDictionary(object):
    
    class TrieNode(object):
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = self.TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, index):
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)