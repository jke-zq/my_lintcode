class Solution {
public:
    /**
     * @param s: A string 
     * @param p: A string includes "?" and "*"
     * @return: A boolean
     */
    bool isMatch(const char *s, const char *p) {
        // write your code here
        //-----Time Limit Exceeded
        // if (*s == 0 || *p == 0) return *s == 0 && *p == 0;
        // if (*p != '*'){
        //     if (*s == *p || *p == '?') return isMatch(++s, ++p);
        //     else return false;
        // }else{
        //     while(*s != 0){
        //         if (isMatch(s+1, p+1)) return true;
        //         ++s;
        //     }
        //     return false;
        // }
        //------Accepted
        // const size_t s_len = strlen(s);
        // const size_t p_len = strlen(p);
        // vector<vector<bool>> table(p_len + 1, vector<bool>(s_len + 1, false));
        // table[0][0] = true;
        // for(int i = 0; i < p_len; ++i){
        //     if (p[i] == '*') table[i+1][0] = true;
        //     else break;
        // }
        // for (int i = 1; i < p_len + 1; ++i){
        //     for(int j = 1; j < s_len + 1; ++j){
        //         table[i][j] = p[i-1] == '*' ? table[i][j-1] || table[i-1][j-1] : table[i-1][j-1] && (p[i-1] == s[j-1] || p[i-1] == '?');
        //     }
        // }
        // return table[p_len][s_len];
        //-------best solution
        int s_pos = 0, p_pos = 0, last_s_pos = -1, last_p_pos = -1;
        int s_len = strlen(s), p_len = strlen(p);
        while (s_pos < s_len){
            if (p_pos < p_len && (p[p_pos] == s[s_pos] || p[p_pos] == '?')){
                ++s_pos;
                ++p_pos;
            }else if (p_pos < p_len && p[p_pos] == '*'){
                ++p_pos;
                last_s_pos = s_pos;
                last_p_pos = p_pos;
            }else if (last_p_pos != -1){
                ++last_s_pos;
                p_pos = last_p_pos;
                s_pos = last_s_pos;
            }else{
                return false;
            }
        }
        while (p_pos < p_len && p[p_pos] == '*') ++p_pos;
        
        return p_pos == p_len;
        
    }
};
