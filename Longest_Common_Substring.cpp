class Solution {
public:    
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        // write your code here
        if(A.length() > B.length()) return longestCommonSubstring(B, A);
        
        vector<vector<int>> table(2, vector<int>(B.length()+1, 0));
        int longest = 0;
        for(int i = 1; i < A.length() + 1; ++i){
            for(int j = 1; j < B.length() + 1; ++j){
                if(A[i-1] == B[j-1]){
                    table[i%2][j] = table[(i-1)%2][j-1] + 1;
                    longest = max(longest, table[i%2][j]);
                }else{
                    table[i%2][j] = 0;
                }
            }
        }
        return longest;
    }
};
