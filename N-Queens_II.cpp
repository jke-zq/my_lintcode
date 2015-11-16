class Solution {
public:
    /**
     * Calculate the total number of distinct N-Queen solutions.
     * @param n: The number of queens.
     * @return: The total number of distinct solutions.
     */
    int totalNQueens(int n) {
        // write your code here
        int result = 0;
        vector<int> tmp;
        find(0, n, tmp, result);
        return result;
    }
    void find(int row, int n, vector<int> &tmp, int &result)
    {
        if (row == n)
        {
            ++result;
        }
        for (int i = 0; i < n; ++i)
        {
            if (check(row, i, tmp))
            {
                tmp.emplace_back(i);
                find(row + 1, n, tmp, result);
                tmp.pop_back();
            }
        }
    }
    bool check(int row, int col, const vector<int> &tmp)
    {
        for (int i = 0; i < tmp.size(); ++i)
        {
            int diff = abs(col - tmp[i]);
            if (diff == 0 || diff == row - i)
            {
                return false;
            }
        }
        return true;
    }
};

