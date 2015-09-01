class Solution {
public:
    /**
     * @param s: A string 
     * @param p: A string includes "." and "*"
     * @return: A boolean
     */
    bool isMatch(const char *s, const char *p) {
        // write your code here
        //recursive
        // if ( *s == 0 || *p == 0) return *s == *p;
        
        // if (*(p + 1) == 0 || p[1] != '*'){
        //     if (*s == *p || *p == '.') return isMatch(s + 1, p + 1);
        //     else return false;
        // }else{
        //     while (*s != 0 && (*p == '.' || *s == *p)){
        //         if (isMatch(s, p + 2)) return true;
        //         ++s;
        //     }
        //     return isMatch(s, p + 2);
        // }
        // // return false;
        //DP
        // int s_len = strlen(s);
        // int p_len = strlen(p);
        //we should use s to match p, that is better.
        // vector<vector<int>> table(2, vector<int>(s_len + 1, false));
        // table[0][0] = true;
        // for (int i = 1; i < p_len + 1; ++i){
        //     table[i % 2][0] = p[i - 1] == '*' && table[(i - 2) % 2][0];
        //     for (int j = 1; j < s_len + 1; ++j){
        //         if (p[i - 1] != '*'){
        //             table[i % 2][j] = table[(i - 1) % 2][j - 1] && (p[i - 1] == s[j - 1] || p[i - 1] == '.');
        //         }else{
        //             table[i % 2][j] = j > 1 && (table[(i - 2) % 2][j] || (table[i % 2][j - 1] && (p[i - 2] == s[j - 1] || p[i - 2] == '.')));
        //         }
        //     }
        // }
        // return table[p_len % 2][s_len];
        // vector<vector<bool>> table(2, vector<bool>(p_len + 1, false));
        // table[0][0] = true;
        // for (int i = 2; i < p_len + 1; ++i){
        //     table[0 % 2][i] = (p[i - 1] == '*') && table[0 % 2][i - 2];
        // }
        // for (int i = 1; i < s_len + 1; ++i){
        //     table[i % 2][0] = false;
        //     for (int j = 1; j < p_len + 1; ++j){
        //         if (p[j - 1] != '*'){
        //             table[i % 2][j] = table[(i - 1) % 2][j - 1] && (p[j - 1] == s[i - 1] || p[j - 1] == '.');
        //         }else{
        //             table[i % 2][j] = j > 1 && (table[i % 2][j - 2] || (table[(i - 1) % 2][j] && (p[j - 2] == s[i - 1] || p[j - 2] == '.')));
        //         }
        //     }
        // }
        // return table[s_len % 2][p_len];
        //other solution:easy to understand and hard to write--I think so.
        const int s_len = strlen(s);
        const int p_len = strlen(p);
        stack<pair<int, int>> last_pos;
        int p_pos = 0, s_pos = 0;
        int last_p_pos = -1, last_s_pos = -1;
        while (s_pos < s_len){
            if (p_pos < p_len && (p_pos == p_len -1 || p[p_pos + 1] != '*') && (p[p_pos] == s[s_pos] || p[p_pos] == '.')){
                ++p_pos;
                ++s_pos;
            }else if (p_pos < p_len - 1 && p[p_pos + 1] == '*'){
                p_pos += 2;
                last_pos.push(pair<int, int>(p_pos, s_pos));
            }else if (!last_pos.empty()){
                tie<int, int>(last_p_pos, last_s_pos) = last_pos.top();
                last_pos.pop();
                while (!last_pos.empty() && p[last_p_pos - 2] != s[last_s_pos] && p[last_p_pos - 2] != '.'){
                    tie<int, int>(last_p_pos, last_s_pos) = last_pos.top();
                    last_pos.pop();
                }
                if (p[last_p_pos - 2] == s[last_s_pos] || p[last_p_pos - 2] == '.'){
                    s_pos = last_s_pos;
                    ++s_pos;
                    p_pos = last_p_pos;
                    last_pos.push(pair<int, int>(last_p_pos, s_pos));
                }else return false;
            }else{
                return false;
            }
        }
        
        while (p_pos < p_len - 1 && p[p_pos + 1] == '*') p_pos += 2;
        return p_pos == p_len;
    }
};
