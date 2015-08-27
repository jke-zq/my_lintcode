class Solution {
public:
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    int numTrees(int n) {
        // write your code here
        vector<int> table(n+1, 0);
        table[1] = 1;
        table[0] = 1;
        for (int i = 2; i <= n; ++i){
            for (int j = 1; j <= i; ++j){
                table[i] += table[i-j] * table[j-1];
            }
        }
        return table[n];
    }
};
