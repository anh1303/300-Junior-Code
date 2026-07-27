from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        num_tasks = len(tasks)
        
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for task in freq if freq[task] == max_freq)
        return max(num_tasks, n*(max_freq - 1) + max_freq + max_count - 1)