class Solution {
    /** 
     * param A : an integer ratated sorted array
     * param target :  an integer to be searched
     * return : an integer
     */
public:
    int search(vector<int> &A, int target) {
        // write your code here
        int s = 0;
        int e = A.size() - 1;
        // while (s <= e){
        //     int m = s + (e - s) / 2;
        //     if (target == A[m]) return m;
        //     if (A[s] > A[e]){
        //         if (A[s] <= target){
        //             if (A[m] > A[s] && A[m] < target){
        //                 s = m + 1;
        //             }else{
        //                 e = m - 1;
        //             }
        //         }else{
        //             if (A[m] < A[e] && A[m] > target){
        //                 e = m - 1;
        //             }else{
        //                 s = m + 1;
        //             }
        //         }
        //     }else{
        //         if (target < A[m]){
        //             e = m - 1;
        //         }else{
        //             s = m + 1;
        //         }
        //     }
        // }
        //to check where is the m
        while (s <= e){
            int m = s + (e - s) / 2;
            if (target == A[m]){
                return m;
            }else if (A[s] <= A[m]){
                if (A[s] <= target && target < A[m]){
                    e = m - 1;
                }else {
                    s = m + 1;
                }
            }else {
                if (A[e] >= target && A[m] < target){
                    s = m + 1;
                }else {
                    e = m - 1;
                }
            }
        }
        return -1;
    }
};
