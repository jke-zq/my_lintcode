class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
public:
    vector<int> searchRange(vector<int> &A, int target) {
        // write your code here
        int s = 0;
        int e = A.size() - 1;
        if (e < 0) return {-1, -1};
        while (s <= e){
            int m = s + (e - s) / 2;
            if (A[m] <= target){
                s = m + 1;
            }else {
                e = m - 1;
            }
        }
        int right = s - 1;
        //check if someone equals target
        if (A[right] != target) return {-1, -1};
        s = 0;
        e = A.size() - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            if (A[m] >= target){
                e = m - 1;
            }else {
                s = m + 1;
            }
        }
        int left = e + 1;
        return vector<int>{left, right};
    }
};
