class Solution {
public:
    /**
     * @param A an integer array
     * @return a long integer
     */
    long long permutationIndex(vector<int>& A) {
        // Write your code here
        long long index = 1L;
        long long factor = 1L;
        for (int i = A.size() - 1; i >= 0; --i)
        {
            int rank = 0;
            for (int j = i + 1; j < A.size(); ++j)
            {
                if (A[i] > A[j])
                {
                    ++rank;
                }
            }
            index += factor * rank;
            factor *= (A.size() - i);
        }
        return index;
    }
};