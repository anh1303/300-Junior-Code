import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++)
        {
            int remainder = target - nums[i];
            if (numToIndex.containsKey(remainder)) {
                return new int[] {numToIndex.get(remainder), i};
            }
            numToIndex.put(nums[i], i);
        }
        return new int[] {-1, -1};
    }
}