class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maximum = [1] * (len(nums) + 1)
        minimum = [1] * (len(nums) + 1)
        result = float('-inf')
        for i in range(1, len(nums) + 1):
            maximum[i] = max(maximum[i-1] * nums[i-1], 
                             minimum[i-1] * nums[i-1], 
                             nums[i-1])
            
            minimum[i] = min(maximum[i-1] * nums[i-1], 
                             minimum[i-1] * nums[i-1], 
                             nums[i-1])
            
            result = max(result, maximum[i])

        return result