class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];
        fill(image, sr, sc, originalColor, color);
        return image;
    }

    private void fill(int[][] image, int r, int c, int originalColor, int newColor)
    {
        int[][] directions = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};
        if (r < 0 || r >= image.length || c < 0 || c>= image[0].length || image[r][c] != originalColor || image[r][c] == newColor)
        {
            return;
        }
        image[r][c] = newColor;
        for (int[] direction: directions)
        {
            fill(image, r + direction[0], c + direction[1], originalColor, newColor);
        }
    }
}