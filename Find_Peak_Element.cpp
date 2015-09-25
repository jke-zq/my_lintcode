class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        // write your code here
        int s = 0;
        int e = A.size() - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            if (A[m - 1] <= A[m]){
                s = m + 1;
            }else{
                e = m - 1;
            }
        }
        return s - 1;
    }
};
