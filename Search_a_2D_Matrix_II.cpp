class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        int m = matrix.size();
        if (!m){
            return 0;
        }
        int n = matrix[0].size();
        if (!n){
            return 0;
        }
        int i = 0, j = n - 1;
        int count = 0;
        while ( i < m && j > -1){
            if (matrix[i][j] == target){
                ++count;
                ++i;
                --j;
            }else if (matrix[i][j] < target){
                ++i;
            }else {
                --j;
            }
        }
        return count;
    }
};

