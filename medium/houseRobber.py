class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        if len(nums) >= 2:
            dp[2] = max(nums[1], nums[0])
            
        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            
        return dp[len(nums)]