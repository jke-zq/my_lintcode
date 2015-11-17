class Solution {
public:
    /**
     * @param nums: a list of integers
     * @return: A integer denote the sum of minimum subarray
     */
    int minSubArray(vector<int> nums) {
        // write your code here
        int s = 0;
        int result = INT_MAX;
        for (const auto& n : nums)
        {
            s += n;
            result = min(result, s);
            s = min(s, 0);
        }
        return result;
    }
};

