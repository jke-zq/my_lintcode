class Solution {
public:
    /**
     * @param nums: An array of integers
     * @return: An array of integers that's next permuation
     */
    vector<int> nextPermutation(vector<int> &nums) {
        // write your code here
        int len = nums.size();
        int i = len - 1;
        while (i > 0){
            if (nums[i] > nums[i - 1]){
                break;
            }
            --i;
        }
        if (i > 0){
            int s = len - 1;
            while (nums[s] <= nums[i - 1]){
                --s;
            }
            swap(nums[i - 1], nums[s]);
        }
        // sort(nums.begin() + i, nums.end());   
        reverse(nums.begin() + i, nums.end());
        return nums;
        
    }
};
