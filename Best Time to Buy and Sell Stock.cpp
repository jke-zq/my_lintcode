class Solution {
public:
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(vector<int> &prices) {
        // write your code here
        int max_pro = 0;
        if (!prices.size())
        {
            return max_pro;
        }
        int least_price = prices[0];
        for (int i = 1; i < prices.size(); ++i)
        {
            // if (prices[i] - least_price > max_pro)
            // {
                // max_pro = prices[i] - least_price;
            // }
            max_pro = max(prices[i] - least_price, max_pro);
            // if (least_price > prices[i])
            // {
                // least_price = prices[i];
            // }
            least_price = min(prices[i], least_price);
        }
        return max_pro;
    }
};
