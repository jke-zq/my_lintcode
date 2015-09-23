class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(int x) {
        // write your code here
        //solution 1
        // int s = 1;
        // int e = x / 2;
        // while (s <= e){
        //     int m = s + (e - s) / 2;
        //     if ( m > x / m){
        //         e = m - 1;
        //     }else{
        //         s = m + 1;
        //     }
        // }
        // return e;//s - 1 is also ok.
        //solution 2
        // int s = 1;
        // int e = x / 2 + 1;
        // while (s < e){
        //     int m = s + (e - s) / 2;
        //     if (m > x / m){
        //         e = m;
        //     }else{
        //         s = m + 1;
        //     }
        // }
        // return s - 1;//e - 1 is also ok, e == s.
        int s = 1;
        int e = x / 2 + 1;
        while (e - s > 1){
            int m = s + (e - s) / 2;
            if (m > x / m){
                e = m;
            }else {
                s = m;
            }
        }
        return s;// e - 1 is ok.
    }
};
