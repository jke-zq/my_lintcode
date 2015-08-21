class Solution {
public:
    /**
     * @param values: a vector of integers
     * @return: a boolean which equals to true if the first player will win
     */
    bool firstWillWin(vector<int> &values) {
        // write your code here
        // read from:http://articles.leetcode.com/2011/02/coins-in-line.html
        if (values.size() % 2 == 0)
            return firstWillWinEven(values);
        int sum = 0;
        for (auto& val : values) sum += val;
        vector<vector<int>> table(3, vector<int>(values.size(), 0));
        //table[n][i] denotes the most sums of numbers which are from ith number to (i+n) th number in values
        for (int n = 0; n < values.size(); ++n){
            for (int i = 0; i + n < values.size(); ++i){
                int a = i + 2 < values.size() && n - 2 > -1 ? table[(n-2)%3][i+2] : 0;
                int b = i + 1 < values.size() && n - 2 > -1 ? table[(n-2)%3][i+1] : 0;
                int c = n - 2 > -1 ? table[(n-2)%3][i] : 0;
                table[n%3][i] = max(values[i] + min(a,b), values[i + n] + min(b, c));
            }
        }
        return table[(values.size()-1)%3][0] > sum - table[(values.size()-1)%3][0];
    }
    bool firstWillWinEven(vector<int>& values){
        int even = 0;
        int odd = 0;
        for (int i = 0; i < values.size(); ++i){
            if (i % 2 == 0) even += values[i];
            else odd += values[i];
        }
        return odd != even;
    }

};
