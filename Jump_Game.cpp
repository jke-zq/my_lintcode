class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    bool canJump(vector<int> A) {
        // write you code here
        //greedy
        // int max_reach = 0;
        // for (int i = 0; i < A.size(); ++i){
        //     // if (i + A[i] > max_reach){
        //     //     max_reach = i + A[i];
        //     // }else if(A[i] == 0 && i == max_reach){
        //     //     break;
        //     // }
        //     if (i > max_reach){
        //         break;
        //     }
        //     max_reach = max(i + A[i], max_reach);
        // }
        // return max_reach > A.size();
        //dp
        vector<int> ret(A.size(), -1);
        ret[0] = A[0];
        for (int i = 1; i < A.size(); ++i){
            if (i < ret[i - 1]){
                ret[i] = max(ret[i - 1], i + A[i]);    
            }
            
        }
        return ret[A.size() - 1] >= 0;
    }
};
