class Solution {
public:
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    int minPathSum(vector<vector<int> > &grid) {
        // write your code here
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<int>> table(2, vector<int>(cols, 0));
        table[0][0] = grid[0][0];
        for(int i = 1; i < cols; ++i)
            table[0][i] = grid[0][i] + table[0][i-1];
        for(int i = 1; i < rows; ++i){
            table[i%2][0] = table[(i-1)%2][0] + grid[i][0];
            for(int j = 1; j < cols; ++j){
                table[i%2][j] = min(table[(i-1)%2][j], table[i%2][j-1]) + grid[i][j];
            }
        }
        return table[(rows-1)%2][cols-1];
    }
};