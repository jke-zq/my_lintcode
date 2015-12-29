class Solution {
public:
    /**
     * @param digits A digital string
     * @return all posible letter combinations
     */
    vector<string> letterCombinations(string& digits) {
        // Write your code here
        vector<string> ret;
        if (digits.empty())
        {
            return ret;
        }
        vector<string> lookups = {"", "", "abc", "def",
                                 "ghi", "jkl", "mno",
                                 "pqrs", "tuv", "wxyz"};
        string combination;
        dolookups(0, combination, ret, lookups, digits);
        return ret;
    }
    void dolookups(int start, string &combination, vector<string> &ret, const vector<string> &lookups, const string &digits)
    {
        if (start == digits.length())
        {
            ret.emplace_back(combination);
            // return;
        }
        else
        {
            for (const auto &c : lookups[digits[start] - '0'])
            {
                combination.push_back(c);
                dolookups(start + 1, combination, ret, lookups, digits);
                combination.pop_back();
            }
        }
    }
};