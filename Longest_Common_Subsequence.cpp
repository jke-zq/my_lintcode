class Solution {
public:
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    int longestCommonSubsequence(string A, string B) {
        // write your code here
        if(A.length() > B.length()) return longestCommonSubsequence(B, A);
        vector<vector<int>> table(2, vector<int>(A.length() + 1, 0));
        int longest = 0;
        for(int i = 1; i < A.length()+1; ++i){
            for(int j = 1; j < B.length()+1; ++j){
                table[i%2][j] = max(table[i%2][j-1], table[(i-1)%2][j]);
                if(A[i-1] == B[j-1]){
                    table[i%2][j] = max(table[(i-1)%2][j-1] + 1, table[i%2][j]);
                }
                longest = max(longest, table[i%2][j]);
            }
        }
        return longest;
    }
};

