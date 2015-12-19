class Solution {
public:
    /**
     * @param s the IP string
     * @return All possible valid IP addresses
     */
    vector<string> restoreIpAddresses(string& s) {
        // Write your code here
        vector<string> ret;
        if (s.length() < 4 )
        {
            return ret;
        }
        string tmp;
        dfs(4, 0, tmp, ret, s);
        return ret;
    }
    void dfs(int parts, int start, string &tmp, vector<string> &ret, string &s)
    {
        if (parts == 0 && start == s.length())
        {
            ret.emplace_back(tmp.substr(1, tmp.length() - 1));
            return;
        }
        int left = s.length() - start;
        for (int i = 1; i < min(4, left + 1); ++i)
        {
            string sub = s.substr(start, i);
            if (atoi(sub.c_str()) <= 255)
            {
                tmp.append(".");
                tmp.append(sub);
                dfs(parts - 1, start + i, tmp, ret, s);
                tmp = tmp.erase(tmp.length() - i - 1, i + 1);
            }
            if (i == 1 && s[start] == '0')
            {
                break;
            }
        }
        
        
    }
};