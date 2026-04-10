class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNonZero = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                if (i == lastNonZero)
                {
                    lastNonZero++;
                }
                else
                {
                    int temp = nums[lastNonZero];
                    nums[lastNonZero] = nums[i];
                    nums[i] = temp;
                    lastNonZero++;
                }

            }
        }
    }
};