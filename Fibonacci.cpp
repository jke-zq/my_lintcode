class Solution{
public:
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    int fibonacci(int n) {
        // write your code here
        if(n == 1) return 0;
        if(n == 2) return 1;
        // return fibonacci(n-1) + fibonacci(n-2);//Time Limit Exceeded
        int s = 0, t = 1, r = 0;
        for(int i = 0; i < n - 2; ++i){
            r = s + t;
            s = t;
            t = r;
        }
        return r;
    }
};

