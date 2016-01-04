class Solution {
public:
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    int maxSquare(vector<vector<int> > &matrix) {
        // write your code here
        //Time Limit Exceeded
        // int rows = matrix.size();
        // int cols = matrix[0].size();
        // int maxLen = 0;
        // vector<int> x;
        // vector<int> y;
        // for(int row = 0; row < rows; ++row){
        //     for(int col = 0; col < cols; ++col){
        //         if(!matrix[row][col]){
        //             continue;
        //         }else{
        //             maxLen = maxLen < 1 ? 1 : maxLen;
        //             if(row < rows - 1 && col < cols - 1 ){
        //                 x.emplace_back(row);
        //                 y.emplace_back(col+1);
        //                 x.emplace_back(row+1);
        //                 y.emplace_back(col+1);
        //                 x.emplace_back(row+1);
        //                 y.emplace_back(col);
        //                 int thisLen = 1;
        //                 checkNext(thisLen, x, y, matrix, rows, cols);
        //                 maxLen = maxLen < thisLen ? thisLen : maxLen;
        //                 x.clear();
        //                 y.clear();                        
        //             }

        //         }
        //     }
        // }
        // return maxLen * maxLen;
        //dp
        if (matrix.empty())
        {
            return 0;
        }
        const int rows = matrix.size(), cols = matrix[0].size();
        vector<vector<int>> dp(2, vector<int>(cols, 0));
        int max_size = 0;
        for (int c = 0; c < cols; ++c)
        {
            dp[0][c] = matrix[0][c];
            max_size = max(max_size, dp[0][c]);
        }
        for (int r = 1; r < rows; ++r)
        {
            dp[r % 2][0] = matrix[r][0];
            max_size = max(max_size, dp[r % 2][0]);
            for (int c = 1; c < cols; ++c)
            {
                if (matrix[r][c])
                {
                    dp[r % 2][c] = min(dp[(r - 1) % 2][c - 1], min(dp[r % 1][c - 1], dp[(r - 1) %
                    2][c])) + 1;
                }
                else
                {
                    dp[r % 2][c] = 0;
                }
                max_size = max(max_size, dp[r % 2][c]);
            }
        }
        return max_size * max_size;
    }
    bool checkNext(int& thisLen, vector<int>& x, vector<int>& y, const vector<vector<int> > &matrix, const int& rows, const int& cols){
        vector<int> tx = move(x);
        vector<int> ty = move(y);
        x.clear();
        y.clear();
        int max_row = *max_element(tx.cbegin(), tx.cend());
        int max_col = *max_element(ty.cbegin(), ty.cend());
        if (max_row == matrix.size() || max_col == matrix[0].size())
        {
            return false;
        }
        int i = 0;
        while(i < tx.size() / 2 + 1){
            if(!matrix[tx[i]][ty[i]]) return false;
            x.emplace_back(tx[i]);
            y.emplace_back(ty[i] + 1);   
            ++i;
        }
        --i;
        x.emplace_back(tx[i] + 1);
        y.emplace_back(ty[i] + 1);
        x.emplace_back(tx[i] + 1);
        y.emplace_back(ty[i]);
        ++i;
        while(i < tx.size()){
            if(!matrix[tx[i]][ty[i]]) return false;
            x.emplace_back(tx[i] + 1);
            y.emplace_back(ty[i]);
            ++i;            
        }
        ++thisLen;
        if(x.size() == tx.size() + 2){
            checkNext(thisLen, x, y, matrix, rows, cols);
        }
        return false;
        
    }
};
