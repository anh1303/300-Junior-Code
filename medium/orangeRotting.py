class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        queue = []
        unrotted_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    unrotted_count += 1
        if unrotted_count == 0:
            return 0
        
        while queue:
            count += 1
            current_rotten_count = len(queue)
            for _ in range(current_rotten_count):
                r, c = queue.pop(0)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        unrotted_count -= 1
            if unrotted_count == 0:
                return count
        return -1
            