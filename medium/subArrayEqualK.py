class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_map = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                result += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return result