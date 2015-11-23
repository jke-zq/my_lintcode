class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: nothing
     */
    void partitionArray(vector<int> &nums) {
        // write your code here
        int left  = 0;
        int right = nums.size() - 1;
        while (left < right)
        {
            while (left < right && nums[left] % 2 == 1)
            {
                ++left;
            }
            
            if (left == right)
            {
                return;
            }
            
            while(left < right && nums[right] % 2 == 0)
            {
                --right;
            }
            
            if (left == right)
            {
                return;
            }
            
            swap(nums[left], nums[right]);
            ++left;
            --right;
        }
    }
};
