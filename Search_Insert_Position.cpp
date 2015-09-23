class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
public:
    int searchInsert(vector<int> &A, int target) {
        // write your code here
        int s = 0;
        int e = A.size() - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            if (A[m] >= target){
                e = m - 1;
            }else {
                s = m + 1;
            }
        }
        return s;
    }
};
