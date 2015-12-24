class Solution {
public:
    /**
     * @param s Roman representation
     * @return an integer
     */
    int romanToInt(string& s) {
        // Write your code here
        unordered_map<char, int> numeral_map = {{'I',    1}, {'V',   5}, {'X',  10},
                                                {'L',   50}, {'C', 100}, {'D', 500},
                                                {'M', 1000}};
        int ret = 0;
        for (int i = 0; i < s.length(); ++i)
        {
            if (i > 0 && numeral_map[s[i]] > numeral_map[s[i - 1]])
            {
                ret += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]];
            }
            else 
            {
                ret += numeral_map[s[i]];
            }
        }
        return ret;
    }
};