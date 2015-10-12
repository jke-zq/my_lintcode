/**
* At first I cant understand this, but later I figure out:
* first divide by 5, and get 5, 10, 15, 20...100...200
* and the divide by second 5, get 25, 50, 100, 200
* and then third 5, get 125, 250
*/
class Solution {
 public:
    // param n : description of n
    // return: description of return 
    long long trailingZeros(long long n) {
        long long num = 0;
        while (n > 0){
            n /= 5;
            num += n;
        }
        return num;
    }
};