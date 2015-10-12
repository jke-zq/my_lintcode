/**
* It is the same as "fast power"; the difference is not a but a % b.
* ***import***: a * a should be long long type
*/ 
class Solution {
public:
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    
    long long doFastPower(long long a, int b, int n){
        if (n == 0){
            return 1 % b;
        }
        if (n % 2 == 1){
            return (a * doFastPower((a * a) % b , b, n / 2)) % b;
        }else {
            return doFastPower((a * a) % b, b, n / 2);
        }
    }
    
    int fastPower(int a, int b, int n) {
        // write your code here
        return doFastPower(a % b, b, n);
    }
};