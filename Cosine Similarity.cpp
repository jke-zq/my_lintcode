class Solution {
public:
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: Cosine similarity.
     */
    double cosineSimilarity(vector<int> A, vector<int> B) {
        // write your code here
        if (A.empty() || B.empty() || (A.size() == 1 && A[0] == 0) || (B.size() == 1 && B[0] == 0))
        {
            return 2.0000;
        }
        double acc_mult = 0;
        double acc_pow_a = 0;
        double acc_pow_b = 0;
        for (int i = 0; i < A.size(); ++i)
        {
            acc_mult += A[i] * B[i];
            acc_pow_a += A[i] * A[i];
            acc_pow_b += B[i] * B[i];
        }
        if (acc_pow_b * acc_pow_a == 0)
        {
            return 2.0000;
        }
        return acc_mult / (sqrt(acc_pow_a) * sqrt(acc_pow_b));
    }
};
