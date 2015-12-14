class Solution {
public:
    void recoverRotatedSortedArray(vector<int> &nums) {
        // write your code here
        int i = 0;
        for (; i < nums.size() - 1 && nums[i] <= nums[i + 1]; ++i)
        {
        }
        
        if (i == nums.size() - 1)
        {
            return;
        }
        //reverse
        reverse(nums.begin(), nums.begin() + i + 1);
        reverse(nums.begin() + i + 1, nums.end());
        reverse(nums.begin(), nums.end());
        //swap
        // swapArray(0, i, nums);
        // swapArray(i + 1, nums.size() - 1, nums);
        // swapArray(0, nums.size() - 1, nums);
    }
    void swapArray(int start, int end, vector<int> &nums)
    {
        if (end <= start)
        {
            return;
        }
        else
        {
            while (start < end)
            {
                swap(nums[start], nums[end]);
                start++;
                end--;
            }
        }
    }
};