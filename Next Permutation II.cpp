class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: return nothing (void), do not return anything, modify nums in-place instead
     */
    void nextPermutation(vector<int> &nums) {
        // write your code here
        int i = nums.size() - 1; 
        while (i > 0 && nums[i] <= nums[i - 1])
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
            while (j > i && nums[j] <= nums[i - 1])
            {
                --j;
            }
            swap(nums[i - 1], nums[j]);
            sort(nums.begin() + i, nums.end());
        }
    }
};