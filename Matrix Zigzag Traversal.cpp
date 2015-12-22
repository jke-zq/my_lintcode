class Solution {
public:
    /**
     * @param matrix: a matrix of integers
     * @return: a vector of integers
     */
    vector<int> printZMatrix(vector<vector<int> > &matrix) {
        // write your code here
        vector<int> ret;
        if (matrix.empty())
        {
            return ret;
        }
        int rows = matrix.size();
        int cols = matrix[0].size();
        for (int i = 0; i < rows + cols - 1; ++i)
        {
            if (i % 2)
            {
                for (int col = min(i, cols - 1); i - col < min(i + 1, rows); --col)
                {
                    ret.emplace_back(matrix[i - col][col]);
                }
            }
            else
            {
                for (int row = min(i, rows - 1); i - row < min(i + 1, cols); --row)
                {
                    ret.emplace_back(matrix[row][i - row]);
                }
            }
        }
        return ret;
    }
};