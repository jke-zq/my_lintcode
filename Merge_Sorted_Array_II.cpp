class Solution {
public:
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        // write your code here
        vector<int> C(A.size() + B.size());
        int i = 0;
        int j = 0;
        while (i < A.size() && j < B.size()){
            if (A[i] < B[j]){
                C[i + j] = A[i];
                ++i;
            }else{
                C[i + j] = B[j];
                ++j;
            }
        }
        
        if (i < A.size()){
            copy(A.cbegin() + i, A.cend(), C.begin() + i + j);
        }else if (j < B.size()){
            copy(B.cbegin() + j, B.cend(), C.begin() + i + j);
        }

        return C;
    }
};
