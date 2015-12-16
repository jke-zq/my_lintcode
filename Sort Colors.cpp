class Solution{
public:
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */    
    void sortColors(vector<int> &nums) {
        // write your code here
        int size = nums.size();
        int left = 0, right = size - 1;
        for (int i = 0; i <= right;)
        {
            // i = max(left, i);
            if (nums[i] == 0)
            {
                swap(nums[i], nums[left]);
                ++left;
                ++i;
            }
            else if (nums[i] == 2)
            {
                swap(nums[i], nums[right]);
                --right;
            }
            else if (nums[i] == 1)
            {
                ++i;
            }
        }
    }
};