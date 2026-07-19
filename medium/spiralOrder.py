class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        num_elements = len(matrix) * len(matrix[0])
        count = 0
        round = 0
        while True:
            for j in range(left + round, right - round + 1):
                result.append(matrix[round][j])
                count += 1
            if count >= num_elements:
                break
            for i in range(round + 1, bottom - round + 1):
                result.append(matrix[i][right - round])
                count += 1
            if count >= num_elements:
                break
            for j in range(right - round - 1, left + round - 1, -1):
                result.append(matrix[bottom - round][j])
                count += 1
            if count >= num_elements:
                break
            for i in range(bottom - round - 1, round, -1):
                result.append(matrix[i][left + round])
                count += 1
            if count >= num_elements:
                break
            round += 1
        return result
            
            
                 