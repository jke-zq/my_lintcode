class Solution {
public:
	/**
	 * @param A : An integer array
	 * @return : An integer 
	 */
    int singleNumberII(vector<int> &A) {
        // write your code here
        //solution 1
        // int one = 0, two = 0;
        // for (auto& i : A){
        //     int new_one = (~i & one) | (i & ~one & ~two);
        //     int new_two = (~i & two) | (i & one);
        //     one = new_one;
        //     two = new_two;
        // }
        // return one;
        //solution 2
        // int one = 0, two = 0, three = 0;
        // for (auto& i : A){
        //     two |= one & i;//first eval &, then |=
        //     one ^= i;//remove the same bit, keep the diff
        //     three = one & two;
        //     //remove the one that occur the one and two same time.
        //     one &= ~three;
        //     two &= ~three;
        // }
        // return one;
        //more general solution 3
        int bits[32] = {0};
        int res = 0;
        for (int i = 0; i < 32; ++i){
            for (auto& a : A){
                bits[i] += (a >> i) & 0x1;
            }
            res |= (bits[i] % 3)<< i;
        }
        return res;
    }
};
