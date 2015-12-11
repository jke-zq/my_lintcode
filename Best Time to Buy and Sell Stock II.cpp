class Solution {
public:
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(vector<int> &prices) {
        // write your code here
        int profits = 0;
        if (prices.empty())
        {
            return profits;
        }
        for (int i = 0; i < prices.size() - 1; ++i)
        {
            profits += max(0, prices[i + 1] - prices[i]);
        }
        return profits;
    }
};