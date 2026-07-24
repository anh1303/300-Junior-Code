class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        max_height = max(height)
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_height * (right - left) <= max_area:
                break
        return max_area