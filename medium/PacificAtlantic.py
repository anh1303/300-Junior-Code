class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pacific = set()
        atlantic = set()
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)
        
        for i in range(len(heights)):
            dfs(i, 0, pacific)
        for j in range(len(heights[0])):
            dfs(0, j, pacific)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic)
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, atlantic)
        
        return list(pacific & atlantic)