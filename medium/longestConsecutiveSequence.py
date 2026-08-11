class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                current += 1
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)