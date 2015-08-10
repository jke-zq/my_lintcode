class Solution {
public:
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    int longestIncreasingContinuousSubsequence(vector<int>& A) {
        // Write your code here
        if(A.empty()) return 0;
        int longest = 1;
        int up = 1, down = 1;
        for(int i = 1; i < A.size(); ++i){
            if(A[i] > A[i-1]){
                ++up;
                down = 1;
            }else{
                ++down;
                up = 1;
            }
            longest = max(up, longest);
            longest = max(down, longest);
        }
        return longest;
    }
};