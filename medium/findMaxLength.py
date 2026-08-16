class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_map = {0: -1}
        prefix = 0
        result = 0
        
        for index, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
                
            if prefix in prefix_map:
                result = max(result, index - prefix_map[prefix])
            else:
                prefix_map[prefix] = index 
        
        return result
                