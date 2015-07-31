class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    void setZeroes(vector<vector<int> > &matrix) {
        // write your code here
        // int rows = matrix.size();
        // if(rows == 0) return;
        // int cols = matrix[0].size();
        // bool isFirst = matrix[0][0] == 0;
        // bool isRow = false;
        // bool isCol = false;
        // for(int i = 0; i < rows; ++i){
        //     if(matrix[i][0] == 0){
        //         isCol = true;
        //         break;
        //     }
        // }
        // for(int i = 0; i < cols; ++i){
        //     if(matrix[0][i] == 0){
        //         isRow = true;
        //         break;
        //     }
        // }
        // for(int i = 0; i < rows; ++i){
        //     for(int j = 0; j < cols; ++j){
        //         if(matrix[i][j] == 0){
        //             matrix[0][j] = 0;
        //             matrix[i][0] = 0;
        //         }
        //     }
        // }
        
        // for(int i = 1; i < rows; ++i){
        //     if(matrix[i][0] == 0){
        //         for(int j = 0; j < cols; ++j){
        //             matrix[i][j] = 0;
        //         }
        //     }
        // }
        // for(int i = 1; i < cols; ++i){
        //     if(matrix[0][i] == 0){
        //         for(int j = 0; j < rows; ++j){
        //             matrix[j][i] = 0;
        //         }
        //     }
        // }
        // if(isFirst){
        //     for(int i = 0; i < cols; ++i){
        //         matrix[0][i] = 0;
        //     }
        //     for(int i = 0; i < rows; ++i){
        //         matrix[i][0] = 0;
        //     }
        // }
        // if(isRow){
        //     for(int i = 0; i < cols; ++i){
        //         matrix[0][i] = 0;
        //     }            
        // }
        // if(isCol){
        //     for(int i = 0; i < rows; ++i){
        //         matrix[i][0] = 0;
        //     }            
        // }
        //good solution
        if(matrix.empty()) return;
        int zero_i = 0;
        int zero_j = 0;
        bool isZero = false;
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < matrix[0].size(); ++j){
                if(matrix[i][j] == 0){
                    if(!isZero){
                        zero_i = i;
                        zero_j = j;
                        isZero = true;
                    }
                    matrix[zero_i][j] = 0;
                    matrix[i][zero_j] = 0;
                }
            }
        }
        if(isZero){
            for(int i = 0; i < matrix.size(); ++i){
                if(i == zero_i) continue;
                for(int j = 0; j < matrix[0].size(); ++j){
                    if(j == zero_j) continue;
                    if(matrix[zero_i][j] == 0 || matrix[i][zero_j] == 0)
                        matrix[i][j] = 0;
                }
            }
            for(int i = 0; i < matrix.size(); ++i)
                matrix[i][zero_j] = 0;
            for(int i = 0; i < matrix[0].size(); ++i)
                matrix[zero_i][i] = 0;
        }
    }
};
