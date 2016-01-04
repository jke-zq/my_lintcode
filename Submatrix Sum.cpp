class Solution {
public:
    /**
     * @param matrix an integer matrix
     * @return the coordinate of the left-up and right-down number
     */
    vector<vector<int>> submatrixSum(vector<vector<int>>& matrix) {
        // Write your code here
        if (matrix.size() < matrix[0].size())
        {
            return horizontal_search(matrix);
        }
        else
        {
            return vertical_search(matrix);
        }
    }
    
    vector<vector<int>> horizontal_search(vector<vector<int>> &matrix)
    {
        for (int i = 0; i < matrix.size(); ++i)
        {
            vector<int> tmp(matrix[0].size());
            for (int j = i; j < matrix.size(); ++j)
            {
                for (int c = 0; c < matrix[0].size(); ++c)
                {
                    tmp[c] += matrix[j][c];
                }
                vector<int> left_right = subArraySumZero(tmp);
                if (!left_right.empty())
                {
                    return {{i, left_right[0]}, {j, left_right[1]}};
                }
            }
        }
        return {};
    }
    
    vector<vector<int>> vertical_search(vector<vector<int>> &matrix)
    {
        for (int left = 0; left < matrix[0].size(); ++left)
        {
            vector<int> tmp(matrix.size());
            for (int right = left; right < matrix[0].size(); ++right)
            {
                for (int row = 0; row < matrix.size(); ++row)
                {
                    tmp[row] += matrix[row][right];
                }
                const auto up_down = subArraySumZero(tmp);
                if (!up_down.empty())
                {
                    return {{up_down[0], left}, {up_down[1], right}};
                }
            }
        }
        return {};
    }
    
    vector<int> subArraySumZero(const vector<int> &array)
    {
        unordered_map<int, int> lookup;
        lookup[0] = -1;
        for (int i = 0, sum = 0; i < array.size(); ++i)
        {
            sum += array[i];
            if (!lookup.emplace(sum, i).second)
            {
                return {lookup[sum] + 1, i};
            }
        }
        return {};
    }
};