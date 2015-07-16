/**
*NOTE:
*     Time Limit Exceeded when testing 9/10 test.
*     I cant solve this problem. Maybe use DP, think later.
*/
class Solution {
public:
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    int maxSquare(vector<vector<int> > &matrix) {
        // write your code here
        int rows = matrix.size();
        int cols = matrix[0].size();
        int maxLen = 0;
        vector<int> x;
        vector<int> y;
        for(int row = 0; row < rows; ++row){
            for(int col = 0; col < cols; ++col){
                if(!matrix[row][col]){
                    continue;
                }else{
                    maxLen = maxLen < 1 ? 1 : maxLen;
                    if(row < rows - 1 && col < cols - 1 ){
                        x.emplace_back(row);
                        y.emplace_back(col+1);
                        x.emplace_back(row+1);
                        y.emplace_back(col+1);
                        x.emplace_back(row+1);
                        y.emplace_back(col);
                        int thisLen = 1;
                        checkNext(thisLen, x, y, matrix, rows, cols);
                        maxLen = maxLen < thisLen ? thisLen : maxLen;
                        x.clear();
                        y.clear();                        
                    }

                }
            }
        }
        return maxLen * maxLen;
    }
    bool checkNext(int& thisLen, vector<int>& x, vector<int>& y, const vector<vector<int> > &matrix, const int& rows, const int& cols){
        vector<int> tx = move(x);
        vector<int> ty = move(y);
        x.clear();
        y.clear();
        int i = 0;
        while(i < tx.size() / 2 + 1){
            if(!matrix[tx[i]][ty[i]]) return false;
            if(ty[i] < cols - 1){
                x.emplace_back(tx[i]);
                y.emplace_back(ty[i] + 1);   
            }
            ++i;
        }
        --i;
        if(tx[i] < rows - 1 && ty[i] < cols - 1){
            x.emplace_back(tx[i] + 1);
            y.emplace_back(ty[i] + 1);
            x.emplace_back(tx[i] + 1);
            y.emplace_back(ty[i]);
        }
        ++i;
        while(i < tx.size()){
            if(!matrix[tx[i]][ty[i]]) return false;
            if(tx[i] < rows - 1){
                x.emplace_back(tx[i] + 1);
                y.emplace_back(ty[i]);
            }
            ++i;            
        }
        ++thisLen;
        if(x.size() == tx.size() + 2){
            checkNext(thisLen, x, y, matrix, rows, cols);
        }
        return false;
        
    }
};
