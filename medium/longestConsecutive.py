class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 1
        for num in nums:
            if num - 1 not in nums:
                count = 1
                start = num
                while start + 1 in nums:
                    count += 1
                    start += 1
                res = max(res, count)
                
        return res