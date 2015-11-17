class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    int maxTwoSubArrays(vector<int> nums) {
        // write your code here
        int len = nums.size();
        vector<int> max_LR(len), max_RL(len);
        int lr_max = INT_MIN, lr_sum = 0;
        for (int i = 0; i < len; ++i)
        {
            lr_sum += nums[i];
            lr_max = max(lr_max, lr_sum);
            lr_sum = max(0, lr_sum);
            max_LR[i] = lr_max;
        }
        
        int rl_max = INT_MIN, rl_sum = 0;
        for (int i = len - 1; i > -1; --i)
        {
            rl_sum += nums[i];
            rl_max = max(rl_max, rl_sum);
            rl_sum = max(0, rl_sum);
            max_RL[i] = rl_max;
        }
        
        int result = INT_MIN;
        for (int i = 0; i < len - 1; ++i)
        {
            result = max(result, max_LR[i] + max_RL[i + 1]);
        }
        return result;
    }
};

