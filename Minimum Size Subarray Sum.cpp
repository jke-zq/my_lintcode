class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    int minimumSize(vector<int> &nums, int s) {
        // write your code here
        int start = -1, sum = 0, min_size = INT_MAX;
        for (int i = 0; i < nums.size(); ++i)
        {
            sum += nums[i];
            while (sum >= s)
            {
                min_size = min(min_size, i - start);
                ++start;
                sum -= nums[start];
            }
        }
        if (min_size == INT_MAX)
        {
            return -1;
        }
        else
        {
            return min_size;
        }
    }
};