class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(grid, r, c, visited):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r, c) in visited):
                return
            visited.add((r, c))
            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r, c - 1, visited)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(grid, r, c, visited)
                    islands += 1
        return islands
                
            
        