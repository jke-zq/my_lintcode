class Solution {
public:
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        // write your code here
        int left = 0;
        int right = A.size();
        while (left < right){
            if (A[left] != elem) ++left;
            else swap(A[left], A[--right]);
        }
        
        return left;
        
    }
};
