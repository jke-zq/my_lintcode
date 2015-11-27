class Solution {
public:
    /**
     * @param matrix a matrix of m x n elements
     * @return an integer array
     */
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        // Write your code here
        vector<int> ret;
        if (matrix.empty())
        {
            return ret;
        }
        int m = matrix.size();
        int n = matrix[0].size();
        int x = 0, y = 0;
        while (m > 0 && n > 0)
        {
            if (m == 1)
            {
                for (int i = 0; i < n; ++i)
                {
                    ret.emplace_back(matrix[x][y]);
                    ++y;
                }
                break;
            }
            else if (n == 1)
            {
                for (int i = 0; i < m; ++i)
                {
                    ret.emplace_back(matrix[x][y]);
                    ++x;
                }
                break;
            }
            
            //top
            for (int i = 0; i < n - 1; ++i)
            {
                ret.emplace_back(matrix[x][y]);
                ++y;
            }
            //right
            for (int i = 0; i < m - 1; ++i)
            {
                ret.emplace_back(matrix[x][y]);
                ++x;
            }
            //buttom
            for (int i = 0; i < n - 1; ++i)
            {
                ret.emplace_back(matrix[x][y]);
                --y;
            }
            //left
            for (int i = 0; i < m - 1; ++i)
            {
                ret.emplace_back(matrix[x][y]);
                --x;
            }
            
            ++x;
            ++y;
            m -= 2;
            n -= 2;
            
        }
        return ret;
    }
};