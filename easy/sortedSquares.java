class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] sortedSq = new int[n];
        int left = 0;
        int right = n - 1;
        int index = n - 1;
        while (left <= right)
        {
            int leftSq = nums[left] * nums[left];
            int rightSq = nums[right] * nums[right];
            if (leftSq > rightSq)
            {
                sortedSq[index] = leftSq;
                left++;
            }
            else
            {
                sortedSq[index] = rightSq;
                right--;
            }
            index--;
        }
        return sortedSq;
    }
}