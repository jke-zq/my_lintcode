class Solution {
public:
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(vector<int> &prices) {
        // write your code here
        int k = 2;
        int n = prices.size();
        vector<int> local(k + 1, 0);
        vector<int> global(k + 1, 0);
        for (int i = 1; i < n; ++i)
        {
            int diff = prices[i] - prices[i - 1];
            for (int j = k; j > 0; --j)
            {
                local[j] = max(global[j - 1] + max(diff, 0), local[j] + diff);
                global[j] = max(global[j], local[j]);
            }
        }
        return global[k];
    }
};