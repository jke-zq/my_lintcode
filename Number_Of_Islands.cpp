
/**
*NOTE:
*    DFS + recursive is a good solution to search the matrix.
*/




class Solution {
public:
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
    int numIslands(vector<vector<bool>>& grid) {
        // Write your code here
        int rows = grid.size();
        if(rows == 0) return 0;
        int cols = grid[0].size();
        int ans = 0;
        for(int row = 0; row < rows; ++row){
            for(int col = 0; col < cols; ++col){
                if(grid[row][col] == false) continue;
                ++ans;
                DFS(grid, row, col, rows, cols);
            }
        }
        return ans;
    }
    void DFS(vector<vector<bool>>& grid, int row, int col, const int rows, const int& cols){
        if(row < 0 || row >= rows || col < 0 || col >= cols){
            return;
        }
        if(grid[row][col] == true){
            grid[row][col] = false;
            DFS(grid, row - 1, col, rows, cols);
            DFS(grid, row + 1, col, rows, cols);
            DFS(grid, row, col + 1, rows, cols);
            DFS(grid, row, col - 1, rows, cols);
        }
    }
};
