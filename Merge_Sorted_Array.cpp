class Solution {
public:
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    void mergeSortedArray(int A[], int m, int B[], int n) {
        // write your code here
        int length = m + n - 1;
        --m; --n;
        while ( m > -1 && n > -1){
            if (A[m] > B[n]){
                A[length] = A[m];
                --m;
            }else{
                A[length] = B[n];
                --n;
            }
            --length;
        }
        while (n > -1){
            A[length] = B[n];
            --length;
            --n;
        }
    }
};
