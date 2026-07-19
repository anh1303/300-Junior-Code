class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        
        target = sum_nums // 2 + 1
        dp = [False] * target
        dp[0] = True
        for num in nums:
            for i in range(target - 1, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[target - 1]