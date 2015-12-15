class Solution {
public:
    /**
     * @param n n pairs
     * @return All combinations of well-formed parentheses
     */
    vector<string> generateParenthesis(int n) {
        // Write your code here
        vector<string> ret;
        string tmp;
        helper(n, n, tmp, ret);
        return ret;
    }
    void helper(int left, int right, string &tmp, vector<string> &ret)
    {
        if (left == 0 && right == 0)
        {
            ret.emplace_back(tmp);
            return;
        }
        if (left > 0)
        {
            tmp.push_back('(');
            helper(left - 1, right, tmp, ret);
            tmp.pop_back();
        }
        if (left < right)
        {
            tmp.push_back(')');
            helper(left, right - 1, tmp, ret);
            tmp.pop_back();
        }
    }
};