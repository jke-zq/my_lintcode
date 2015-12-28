class Solution {
public:
    /**
      * @param n: n
      * @param k: the kth permutation
      * @return: return the k-th permutation
      */
    string getPermutation(int n, int k) {
    
        vector<int> nums;
        int groups = 1;
        for (int i = 1; i <= n; ++i)
        {
            groups *= i;
            nums.emplace_back(i);
        }
        
        --k;
        stringstream ret;
        while (n > 0)
        {
            groups /= n;
            int idx = k / groups;
            ret << nums[idx];
            nums.erase(nums.begin() + idx);
            k %= groups;
            --n;
        }
        return ret.str();
    }
       
};