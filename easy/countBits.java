class Solution {
    public int[] countBits(int n) {
        int[] results = new int[n+1];
        for (int i = 1; i <= n; i++)
        {
            results[i] = results[i>>1] + (i & 1);
        }
        return results;
    }
}