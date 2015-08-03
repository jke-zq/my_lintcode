class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    void rotate(vector<vector<int> > &matrix) {
        // write your code here
        if(matrix.empty()) return;
        int rows = matrix.size();
        for(int i = 0; i < rows; ++i){
            for(int j = 0; j < i; ++j){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
                
            }
        }
        
        for(int i = 0; i < rows; ++i){
            int start = 0;
            int end = rows-1;
            while(start < end){
                int temp = matrix[i][start];
                matrix[i][start] = matrix[i][end];
                matrix[i][end] = temp;
                ++start;
                --end;
            }
        }
    }
};
