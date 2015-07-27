class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        // write your code here
        // int right = n & ((0x1 << i) - 1);
        // int left = j >= 31 ? 0 : (n >> (j+1)) << (j+1);
        // return left | m << i | right;
        unsigned int tag = 0xffffffff;
        int right = i == 0 ? 0 : n & (tag >> (32-i));
        int left = j >= 31 ? 0 : (n >> (j+1)) << (j+1);
        return left | m << i | right;
    }
};
