class Solution {
public:    
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    int maxSubArray(vector<int> nums) {
        // write your code here
        // int s = nums[0];
        // int result = nums[0];
        // for (int i = 1; i < nums.size(); ++i)
        // {
        //     if (s < 0 || s + nums[i] < 0)
        //     {
        //         s = nums[i];
        //     }
        //     else
        //     {
        //         s += nums[i];
        //     }
        //     result = max(result, s);
        // }
        // return result;
        //good codes
        int s = 0;
        int result = INT_MIN;
        for (const auto &n : nums)
        {
            s += n;
            result = max(result, s);
            s = max(s, 0);
        }
        return result;
    }
};

