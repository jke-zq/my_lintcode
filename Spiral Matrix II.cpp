class Solution {
public:
    /**
     * @param n an integer
     * @return a square matrix
     */
    vector<vector<int>> generateMatrix(int n) {
        // Write your code here
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        int number = 1;
        int m = n;
        int x = 0, y = 0;
        while (m > 0 && n > 0)
        {
            if (m == 1)
            {
                for (int i = 0; i < n; ++i)
                {
                    matrix[x][y] = number;
                    ++number;
                    ++y;
                }
                break;
            }
            else if (n == 1)
            {
                for (int i = 0; i < m; ++i)
                {
                    matrix[x][y] = number;
                    ++number;
                    ++x;
                }
                break;
            }
            for (int i = 0; i < n - 1; ++i)
            {
                matrix[x][y] = number;
                ++number;
                ++y;
            }
            for (int i = 0; i < m - 1; ++i)
            {
                matrix[x][y] = number;
                ++number;
                ++x;
            }
            for (int i = 0; i < n - 1; ++i)
            {
                matrix[x][y] = number;
                ++number;
                --y;
            }
            for (int i = 0; i < m - 1; ++i)
            {
                matrix[x][y] = number;
                ++number;
                --x;
            }
            ++x;
            ++y;
            m -= 2;
            n -= 2;
        }
        return matrix;
    }
};
