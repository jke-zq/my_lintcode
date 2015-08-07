class Solution {
public:
    /**
     * @param obstacleGrid: A list of lists of integers
     * @return: An integer
     */ 
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        // write your code here
        int rows = obstacleGrid.size();
        int cols = obstacleGrid[0].size();
        vector<vector<int>> table(2, vector<int>(cols, 0));
        table[0][0] = obstacleGrid[0][0] == 1 ? 0 : 1;
        for(int i = 1; i < cols; ++i)
            table[0][i] = obstacleGrid[0][i] == 1 ? 0 : table[0][i-1];
        for(int i = 1; i < rows; ++i){
            table[i%2][0] = obstacleGrid[i][0] == 1 ? 0 : table[(i-1)%2][0];
            for(int j = 1; j < cols; ++j){
                table[i%2][j] = obstacleGrid[i][j] == 1 ? 0 : table[(i-1)%2][j] + 
                table[i%2][j-1];
            }
        }
        return table[(rows-1)%2][cols-1];
    }
};
