from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        count = Counter(words)
        words_set = list(count.keys())
        words_set.sort(key = lambda x: (-count[x], x))
        
        return words_set[:k]