class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: An integer denote to find k non-overlapping subarrays
     * @return: An integer denote the sum of max k non-overlapping subarrays
     */
    int maxSubArray(vector<int> nums, int k) {
        // write your code here
        int n = nums.size();
        vector<vector<int>> table(n + 1, vector<int>(n + 1, INT_MIN));
        table[0][0] = 0;
        for (int i = 1; i < n + 1; ++i){
            table[i][0] = 0;
            for (int j = 1; j < min(i, k) + 1; ++j){
                table[i][j] = table[i - 1][j];
                int max_from_p = 0;
                for (int p = i; p > j - 1; --p){
                    max_from_p = max(0, max_from_p) + nums[p - 1];
                    table[i][j] = max(table[i][j], table[p - 1][j - 1] + max_from_p);
                }
            }
        }
        return table[n][k];
    }
};

