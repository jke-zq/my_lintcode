class Solution {
public:
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    vector<vector<string> > solveNQueens(int n) {
        // write your code here
        //ugly
        // vector<vector<string>> ret;
        // vector<vector<int>> path(n, vector<int>(n, 0));
        // helper(0, n, path, ret);
        // return ret;
        ////what we need is the col_index, so store the col_index.
        vector<vector<string>> ret;
        vector<int> col_index(n, 0);
        helper2(0, n, col_index, ret);
        return ret;
    }
    
    void helper2(int row, int n, vector<int> &col_index, vector<vector<string>> &ret)
    {
        if (row == n){
            ret.emplace_back(getSol(col_index));
        }
        else
        {
            for (int i = 0; i < n; ++i)
            {
                col_index[row] = i;
                if (isSol(row, col_index))
                {
                    helper2(row + 1, n, col_index, ret);
                }
            }
        }
    }
    
    bool isSol(int row, const vector<int> &co_index)
    {
        for (int i = 0; i < row; ++i)
        {
            int diff = abs(co_index[i] - co_index[row]);
            if (diff == 0 || diff == row - i)
            {
                return false;
            }
        }
        return true;
    }
    
    vector<string> getSol(const vector<int> &col_index)
    {
        vector<string> sol;
        for (auto &index : col_index)
        {
            string s(col_index.size(), '.');
            s[index] = 'Q';
            sol.emplace_back(s);
        }
        return sol;
    }
    
    // void helper(int row, int n, vector<vector<int>> &path, vector<vector<string>> &ret)
    // {
    //     if (row == n)
    //     {
    //         ret.emplace_back(topath(path));
    //         return;
    //     }
    //     for (int i = 0; i < n; ++i)
    //     {
    //         path[row][i] = 1;
    //         if (check(path, row, i))
    //         {
    //             helper(row + 1, n, path, ret);    
    //         }
    //         path[row][i] = 0;
    //     }
    // }
    
    // bool check(const vector<vector<int>> &path, int row, int col)
    // {
    //     for (int i = 0; i < row; ++i)
    //     {
    //         int ci = -1;
    //         for (int z = 0; z < path.size(); ++z)
    //         {
    //             if (path[i][z] == 1)
    //             {
    //                 ci = z;
    //                 break;
    //             }

    //         }
    //         if (ci == col || abs(ci - col) == row - i){
    //             return false;
    //         }
    //     }
    //     return true;
    // }
    
    // vector<string> topath(const vector<vector<int>> &path)
    // {
    //     vector<string> ret(path.size(), string(path.size(), '.'));
    //     for (int i = 0; i < path.size(); ++i)
    //     {
    //         for (int j = 0; j < path[i].size(); ++j)
    //         {
    //             if (path[i][j] == 1){
    //                 ret[i][j] = 'Q';
    //             }
    //         }
    //     }
    //     return ret;
    // }
};

