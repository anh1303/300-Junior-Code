class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        def backtrack(current_path, remaining, start):
            if remaining == 0:
                solutions.append(list(current_path))
                return
            elif remaining < 0:
                return     
            for i in range(start, len(candidates)):
                current_path.append(candidates[i])
                backtrack(current_path, remaining - candidates[i], i)
                current_path.pop()   
        backtrack([], target, 0)
        return solutions