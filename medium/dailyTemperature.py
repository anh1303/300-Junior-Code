class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        if temperatures is None:
            return []
        
        results = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if stack:
                while stack and temp > temperatures[stack[-1]]:
                    results[stack[-1]] = index - stack[-1]
                    stack.pop()
            stack.append(index)
            
        return results