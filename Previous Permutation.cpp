class Solution {
public:
    /**
     * @param nums: An array of integers
     * @return: An array of integers that's previous permuation
     */
    vector<int> previousPermuation(vector<int> &nums) {
        // write your code here
        int i = nums.size() - 1;
        while (i > 0 && nums[i] >= nums[i - 1])
        {
            --i;
        }
        if (i == 0)
        {
            reverse(nums.begin(), nums.end());
        }
        else
        {
            int j = nums.size() - 1;
            while (nums[j] > nums[i - 1])
            {
                --j;
            }
            swap(nums[i - 1], nums[j]);
            sort(nums.begin() + i, nums.end(), greater<int>());
        }
        return nums;
    }
};