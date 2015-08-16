class Solution {
public:
    /**
     * @param A an integer matrix
     * @return  an integer
     */
    int longestIncreasingContinuousSubsequenceII(vector<vector<int>>& A) {
        // Write your code here
        //NOTE:fill(vector<vector<int>>& A, int row, int col, vector<vector<int>>& max_len, int preVal) will case TLE
        if(A.empty()) return 0;
        int rows = A.size();
        int cols = A[0].size();
        vector<vector<int>> max_len(rows, vector<int>(cols, 0));
        int longest = 1;
        for(int i = 0; i < rows; ++i){
            for(int j = 0; j < cols; ++j){
                if(max_len[i][j] == 0){
                    longest = max(longest, fill(A, i, j, max_len, INT_MAX));
                }
            }
        }
        return longest;
    }
    int fill(vector<vector<int>>& A, int row, int col, vector<vector<int>>& max_len, int preVal){
        if(row < 0 || row >= A.size() || col < 0 || col >= A[0].size() || preVal <= A[row][col]) return 0;
        if(max_len[row][col] > 0) return max_len[row][col];
        vector<pair<int, int>> dics = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for(auto& d : dics){
            max_len[row][col] = max(max_len[row][col], fill(A, row + d.first, col + d.second, max_len, A[row][col]) + 1);
        }
        return max_len[row][col];
    }
};
