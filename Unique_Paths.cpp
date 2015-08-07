class Solution {
public:
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    int uniquePaths(int m, int n) {
        // wirte your code here
        if(m > n) return uniquePaths(n, m);
        vector<vector<int>> table(2, vector<int>(n, 0));
        for(int i = 0; i < n; ++i)
            table[0][i] = 1;
        for(int i = 1; i < m; ++i){
            table[i%2][0] = 1;
            for(int j = 0; j < n; ++j){
                table[i%2][j] = table[(i-1)%2][j] + table[i%2][j-1];
            }
        }
        return table[(m-1)%2][n-1];
    }
};

