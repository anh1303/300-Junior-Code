import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix_sum.append(self.total)


    def pickIndex(self) -> int:
        ran_num = random.randint(1, self.total)
        left = 0
        right = len(self.w) - 1
        result = -1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] >= ran_num:
                right = mid
            else:
                left = mid + 1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()