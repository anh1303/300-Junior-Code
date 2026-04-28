import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (mat[i][j] == 0)
                {
                    dist[i][j] = 0;
                    queue.offer(new int[]{i, j});
                }
                else
                {
                    dist[i][j] = -1;
                }
            }
        }
        while (!queue.isEmpty())
        {
            int[] cell = queue.poll();
            int x = cell[0];
            int y = cell[1];
            int [][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (int[] dir : directions)
            {
                int newX = x + dir[0];
                int newY = y + dir[1];
                if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && dist[newX][newY] == -1)
                {
                    dist[newX][newY] = dist[x][y] + 1;
                    queue.offer(new int[]{newX, newY});
                }
            }
        }
        return dist;
    }
}