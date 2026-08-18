class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(str, open_count, close_count, n):
            if len(str) == 2*n:
                result.append(str)
                return
            if open_count < n:
                backtrack(str + '(', open_count + 1, close_count, n)
            if close_count < open_count:
                backtrack(str + ')', open_count, close_count + 1, n)
        backtrack('', 0, 0, n)
        return result