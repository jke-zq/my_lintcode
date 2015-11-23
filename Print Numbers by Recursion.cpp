class Solution {
public:
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    vector<int> numbersByRecursion(int n) {
        // write your code here
        vector<int> ret;
        // if (n == 0)
        // {
        //     return ret;
        // }
        // doHelper(1, pow(10, n) - 1, ret);
        // return ret;
        doHelper(0, n, ret);
        return ret;
    }
    void doHelper(int depth, int n, vector<int> &ret)
    {
        if (depth == n)
        {
            return;
        }
        else if (depth == 0)
        {
            for (int i = 1; i < 10; ++i)
            {
                ret.emplace_back(i);
            }
        }
        else
        {
            size_t count = ret.size();
            for (int i = 1; i < 10; i++)
            {
                int basic = i * pow(10, depth);
                ret.emplace_back(basic);
                for (int j = 0; j < count; ++j)
                {
                    ret.emplace_back(ret[j] + basic);
                }
            }
        }
        doHelper(depth + 1, n, ret);
    }
    // void doHelper(int n, int largest, vector<int> &ret)
    // {
    //     if (n > largest)
    //     {
    //         return;
    //     }
    //     else
    //     {
    //         ret.emplace_back(n);
    //         doHelper(n + 1, largest, ret);
    //     }
    // }
};
