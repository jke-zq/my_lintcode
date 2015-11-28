class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     */
    string reverseWords(string s) {
        // write your code here
        // vector<string> ret;
        // int i = 0;
        // while(i < s.length() && s[i] == ' ')
        // {
        //     ++i;
        // }
        // string tmp = "";
        // for (; i < s.length();)
        // {
        //     if (s[i] == ' ')
        //     {
        //         ret.emplace_back(move(tmp));
        //         while(i < s.length() && s[i] == ' ')
        //         {
        //             ++i;
        //         }
                
        //     }
        //     else
        //     {
        //         tmp += s[i];
        //         ++i;
        //     }
        // }
        // if (tmp != "")
        // {
        //     ret.emplace_back(move(tmp));    
        // }
        
        // reverse(ret.begin(), ret.end());
        // string ret_s;
        // for (auto &r : ret)
        // {
        //     ret_s += r;
        //     ret_s += ' ';
        // }
        // return ret_s;
        ////other codes, just for practising
        reverse(s.begin(), s.end());
        size_t start = 0, end;
        while ((end = s.find(" ", start)) != string::npos)
        {
            reverse(s.begin() + start, s.begin() + end);
            start = end + 1;
        }
        
        reverse(s.begin() + start, s.end());
        
        if ((start = s.find_first_not_of(" ")) != string::npos)
        {
            return s.substr(start);
        }
        else
        {
            return s;
        }
        
        
    }
};
