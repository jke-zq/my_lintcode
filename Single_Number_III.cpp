class Solution {
public:
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    vector<int> singleNumberIII(vector<int> &A) {
        // write your code here
        //get x_xor_y
        int x_xor_y = 0;
        for (auto& a : A){
            x_xor_y ^= a;
        }
        //get the lowest one in bit form
        int bits = x_xor_y & ~(x_xor_y - 1);
        int x = 0;
        for (auto& a : A){
            if (a & bits){
                x ^= a;
            }
        }
        return {x, x_xor_y ^ x};
        
    }
};
