class Solution {
public:
    /*
     * param k : As description.
     * param n : As description.
     * return: How many k's between 0 and n.
     */
    int digitCounts(int k, int n) {
        // write your code here
        int left = n, cnt = 0, right = 0, mult = 1;
        while (left > 0)
        {
            int cur = left % 10;
            left /= 10;
            right = n % mult;
            cnt += left * mult;
            if (k < cur)
            {
                cnt += mult;
            }
            else if (k == cur)
            {
                cnt += right + 1;
            }
            //because that the first digit cant be zero, but zero
            if (k == 0 && mult > 1)
            {
                cnt -= mult;
            }
            
            mult *= 10;
        }
        return cnt;
    }
};
