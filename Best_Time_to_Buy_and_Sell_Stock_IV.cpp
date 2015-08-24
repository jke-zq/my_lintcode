class Solution {
public:
    /**
     * @param k: An integer
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(int k, vector<int> &prices) {
        // write your code here
        int n = prices.size();
        //just need the most (prices.size() / 2 ) transactions
        if (k >= prices.size() / 2){
            int profit = 0;
            for(int i = 0; i < n - 1; ++i){
                profit += max(0, prices[i+1] - prices[i]);
            }
            return profit;
        }
        vector<int> local(k+1, 0);
        vector<int> global(k+1, 0);
        for(int i = 1; i < n; ++i){
            int diff = prices[i] - prices[i-1];
            for(int j = k; j > 0; --j){
                local[j] = max(global[j-1] + max(diff, 0), local[j] + diff);
                global[j] = max(local[j], global[j]);
            }
        }
        return global[k];
    }
};
