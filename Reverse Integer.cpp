class Solution {
public:
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    int reverseInteger(int n) {
        // Write your code here
        int sign = 1;
        if (n < 0)
        {
            sign = -1;
            n *= -1;
        }
        long new_n = 0;
        while (n > 0)
        {
            new_n *= 10;
            new_n += n % 10;
            n = n / 10;
        }
        if (new_n > INT_MAX)
        {
            return 0;
        }
        else
        {
            return sign * new_n;
        }
    }
};
