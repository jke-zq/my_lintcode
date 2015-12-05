class Solution {
public:
    /**
     * @param x the base number
     * @param n the power number
     * @return the result
     */
    double myPow(double x, int n) {
        // Write your code here
        if (n == 0)
        {
            return 1;
        }
        if (n < 0)
        {
            return 1 / myPow(x, -1 * n);
        }
        if (n % 2 == 0)
        {
            return myPow(x * x, n / 2);
        }
        else
        {
            return x * myPow(x * x, n / 2);
        }
    }
};
