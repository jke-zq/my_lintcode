class Solution {
    /** 
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean 
     */
public:
    bool search(vector<int> &A, int target) {
        // write your code here
        if (A.empty()) return false;
        int s = 0;
        int e = A.size() - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            if (A[m] == target){
                return true;
            }else if (A[s] < A[m]){
                if (A[s] <= target && A[m] > target){
                    e = m - 1;
                }else {
                    s = m + 1;
                }
            }else if(A[s] > A[m]) {
                if (A[e] >= target && A[m] < target){
                    s = m + 1;
                }else {
                    e = m - 1;   
                }
            }else {
                ++s;
            }
        }
        return false;
    }
};
