class Solution {
public:
    /**
     * @param values: a vector of integers
     * @return: a boolean which equals to true if the first player will win
     */
    bool firstWillWin(vector<int> &values) {
        // write your code here
        vector<int> table(5, 0);
        int sum = 0;
        for(int i = values.size() - 1; i > -1; --i){
            sum += values[i];
            int a = i + 1 < values.size() ? values[i+1] : 0;
            int b = i + 2 < values.size() ? table[(i+2)%5] : 0;
            int c = i + 3 < values.size() ? table[(i+3)%5] : 0;
            int d = i + 4 < values.size() ? table[(i+4)%5] : 0;
            table[i%5] = max(values[i] + min(b, c), values[i] + a + min(c,d));
        }
        return table[0] > sum - table[0];
    }
};