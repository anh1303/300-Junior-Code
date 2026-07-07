class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = len(nums)
        suffix = [1] * count
        prefix = [1] * count
        for i in range(1, count):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(count - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        result = [1] * count
        for i in range(count):
            result[i] = prefix[i] * suffix[i]
        return result