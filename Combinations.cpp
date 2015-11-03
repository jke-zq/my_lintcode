class Solution {
public:
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    vector<vector<int> > combine(int n, int k) {
        // write your code here
        vector<vector<int>> ret;
        vector<int> tmp;
        // helper(1, k, n, &tmp, &ret);
        helperRef(1, k, n, tmp, ret);
        return ret;
    }
private:
    // void helper(int start, int k, int n, vector<int> *tmp, vector<vector<int>> *ret)
    // {
    //     if (tmp->size() == k)
    //     {
    //         ret->emplace_back(*tmp);
    //         return;
    //     }
    //     for (int i = start; i < n + 1; ++i)
    //     {
    //         tmp->emplace_back(i);
    //         helper(i + 1, k, n, tmp, ret);
    //         tmp->pop_back();
    //     }
    // }
    void helperRef(int start, int k, int n, vector<int> &tmp, vector<vector<int>> &ret)
    {
        if (tmp.size() == k)
        {
            //cant use move func
            ret.emplace_back(tmp);
            return;
        }
        for (int i = start; i < n + 1; ++i)
        {
            tmp.emplace_back(i);
            helperRef(i + 1, k, n, tmp, ret);
            tmp.pop_back();
        }
    }
};
