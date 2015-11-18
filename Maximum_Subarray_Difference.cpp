class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: An integer indicate the value of maximum difference between two
     *          Subarrays
     */
    int maxDiffSubArrays(vector<int> nums) {
        // write your code here
        int len = nums.size();
        vector<int> max_LR(len), max_RL(len), min_LR(len), min_RL(len);
        
        int lr_max = INT_MIN, lr_sum = 0;
        for (int i = 0; i < len; ++i)
        {
            lr_sum += nums[i];
            lr_max = max(lr_max, lr_sum);
            lr_sum = max(lr_sum, 0);
            max_LR[i] = lr_max;
        }
        
        int rl_max = INT_MIN, rl_sum = 0;
        for (int i = len - 1; i > -1; --i)
        {
            rl_sum += nums[i];
            rl_max = max(rl_max, rl_sum);
            rl_sum = max(rl_sum, 0);
            max_RL[i] = rl_max;
        }
        
        int lr_min = INT_MAX;
        lr_sum = 0;
        for (int i = 0; i < len; ++i)
        {
            lr_sum += nums[i];
            lr_min = min(lr_min, lr_sum);
            lr_sum = min(lr_sum, 0);
            min_LR[i] = lr_min;
        }
        
        int rl_min = INT_MAX;
        rl_sum = 0;
        for (int i = len - 1; i > -1; --i)
        {
            rl_sum += nums[i];
            rl_min = min(rl_min, rl_sum);
            rl_sum = min(rl_sum, 0);
            min_RL[i] = rl_min;
        }
        
        int result = INT_MIN;
        for (int i = 0; i < len - 1; ++i)
        {
            result = max(result, abs(max_LR[i] - min_RL[i + 1]));
            result = max(result, abs(max_RL[i + 1] - min_LR[i]));
        }
        return result;
    }
};

