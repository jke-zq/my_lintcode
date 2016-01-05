class Solution {
public:
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    double findMedianSortedArrays(vector<int> A, vector<int> B) {
        // write your code here
        if ((A.size() + B.size()) % 2 == 1)
        {
            return findKthInTwoSortedArray(B, A, (A.size() + B.size() + 1) / 2);
        }
        else
        {
            return (findKthInTwoSortedArray(B, A, (A.size() + B.size()) / 2) + findKthInTwoSortedArray(B, A, (A.size() + B.size()) / 2 + 1)) / 2.0;
        }
    }
    int findKthInTwoSortedArray(vector<int> &A, vector<int> &B, int k)
    {
        int m = A.size();
        int n = B.size();
        if (m > n)
        {
            return findKthInTwoSortedArray(B, A, k);
        }
        int left = 0;
        int right = m;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            int mid_B = k - 1 - mid;
            if (mid_B >= 0 && mid_B < B.size() && A[mid] > B[mid_B])
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        
        int min_A = left - 1 >= 0 ? A[left - 1] : INT_MIN;//if INT_MIN, then kth is in the B array.
        //left == right, then mid = left, and mid_B = k - 1 - left.
        int value_B = k - 1 - left >= 0 ? B[k - 1  - left] : INT_MIN;
        return max(min_A, value_B);
    }
};
