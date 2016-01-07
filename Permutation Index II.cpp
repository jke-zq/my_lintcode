class Solution {
public:
    /**
     * @param A an integer array
     * @return a long integer
     */
    long long permutationIndexII(vector<int>& A) {
        // Write your code here
        long long ret = 1L;
        map<int, int> counts;
        long long factor = 1L;
        for (int i = A.size() - 1; i >= 0; --i)
        {
            ++counts[A[i]];
            for (const auto &c : counts)
            {
                if (c.first == A[i])
                {
                    break;
                }
                else
                {
                    //make the Str.first as the first one in the permutation, then the left will has (Str.second - 1) Str(s), and counts[A[i]] A[i](s). So, the fator will be:
                    //factor / counts[A[i]] * Str.second. descrese one Str, add one A[i].
                    ret += factor * c.second / counts[A[i]];
                }
            }
            factor = factor * (A.size() - i) / counts[A[i]];
        }
        return ret;
    }
};