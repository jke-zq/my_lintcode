class Solution {
public:
    /**
     * @param A: An integer array.
     * @return: void
     */
    void rerange(vector<int> &A) {
        // write your code here
        // sort(A.begin(), A.end());
        // int mid = 0;
        // while (A[mid] < 0)
        // {
        //     ++mid;
        // }
        // if (mid * 2 < A.size())
        // {
        //     reverse(A.begin(), A.end());
        //     mid = A.size() - mid;
        //     swap(A[mid], A[A.size() - 1]);
        // }
        // size_t left = 1;
        // size_t right = 2 * mid - 2;
        // while (left < right)
        // {
        //     swap(A[left], A[right]);
        //     left += 2;
        //     right -= 2;
        // }
        //good solution
        int posCount = 0;
        for (const auto &a : A)
        {
            posCount += a > 0 ? 1 : 0;
        }
        
        int expectPos = 2 * posCount > A.size() ? true : false;
        int pos = 0, neg = 0, i = 0;
        while (i < A.size())
        {
            while (pos < A.size() && A[pos] > 0)
            {
                ++pos;
            }
            while (neg < A.size() && A[neg] < 0)
            {
                ++neg;
            }
            
            if (expectPos && neg < A.size())
            {
                swap(A[i], A[neg]);
                ++i;
                ++neg;
            }
            else if (!expectPos && pos < A.size())
            {
                swap(A[i], A[pos]);
                ++i;
                ++pos;
            }
            expectPos = !expectPos;
        }
    }
};