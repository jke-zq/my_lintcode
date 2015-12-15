class Solution {
public:
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
    int divide(int dividend, int divisor) {
        // Write your code here
        long long dvd = llabs(dividend);
        long long dvs = llabs(divisor);
        long long ret = 0;
        long long mult = 1;
        while (dvd > dvs)
        {
            dvs <<= 1;
            mult <<= 1;
        }
        
        while (dvd >= llabs(divisor))
        {
            while (dvd >= dvs)
            {
                dvd -= dvs;
                ret += mult;
            }
            dvs >>= 1;
            mult >>= 1;
        }
        if ((dividend < 0) ^ (divisor < 0))
        // if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0))
        {
            return -ret;
        }
        else
        {
            return min(ret, static_cast<long long>(INT_MAX));
        }
        
    }
};