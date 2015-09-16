class Solution {
public:
    /**    
     * @param A: a vector of integers
     * @return: an integer
     */
    int firstMissingPositive(vector<int> A) {
        // write your code here
        if (A.empty()) return 1;
        int length = A.size();
        for (int i = 0; i < length;){
            if (A[i] != A[A[i] - 1] && A[i] <= length && A[i] > 0){
                swap(A[A[i] - 1], A[i]);
            }else{
                ++i;
            }
        }
        for (int i = 0; i < length; ++i){
            if (A[i] != i + 1) return i + 1;
        }
        return length + 1;
    }
};