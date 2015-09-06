class Solution {
public:
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    bool wordBreak(string s, unordered_set<string> &dict) {
        // write your code here
        if (s == "") return true;
        int s_len = s.length();
        //Memory Limit Exceeded
        //vector<vector<bool>> table(s_len, vector<bool>(s_len, false));
        //filter--without TLE
        unordered_set<char> chrs;
        for (const auto& word : dict){
            for (const auto& c : word){
                chrs.insert(c);
            }
        }
        for (const auto& c : s){
            if (chrs.find(c) == chrs.end()) return false;
        }
        vector<vector<bool>> table(s_len, vector<bool>(1, false));
        for (int i = 0; i < s_len; ++i){
            for (int j = i; j > -1; --j){
                if (dict.count(s.substr(j, i - j + 1)) > 0 && (j < 1 || table[j - 1][0])){
                //this is better
                // if ((j < 1 || table[j - 1][0]) && dict.count(s.substr(j, i - j + 1)) > 0){
                    table[i][0] = true;
                    //without TLE
                    break;
                }
                    
            }
        }
        return table[s_len - 1][0];
    }
};
