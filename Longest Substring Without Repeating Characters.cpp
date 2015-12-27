class Solution {
public:
    /**
     * @param s: a string
     * @return: an integer 
     */
    int lengthOfLongestSubstring(string s) {
        // write your code here
        unordered_map<char, size_t> last_occur;
        size_t startId = 0, ret = 0;
        for (size_t i = 0; i < s.length(); ++i)
        {
            if (last_occur.find(s[i]) == last_occur.end())
            {
                last_occur.emplace(s[i], i);
            }
            else
            {
                if (last_occur[s[i]] >= startId)
                {
                    ret = max(ret, i - startId);
                    startId = last_occur[s[i]] + 1;
                }
                last_occur[s[i]] = i;
            }
        }
        ret = max(ret, s.length() - startId);
        return ret;
    }
};