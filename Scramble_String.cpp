class Solution {
public:
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
    bool isScramble(string& s1, string& s2) {
        // Write your code here
        //not DP, just recursive
        // return doHelper(s1, 0, s1.size(), s2, 0, s2.size());
        
        //DP
        if(s1.length() != s2.length()) return false;
        if(s1 == s2) return true;
        const auto length = s1.length();
        vector<vector<vector<bool>>> table(length+1, vector<vector<bool>>(length, vector<bool>(length, false)));
        for(int i = 0; i < length; ++i){
            for(int j = 0; j < length; ++j){
                if(s1[i] == s2[j])
                    table[1][i][j] = true;
            }
        }
        for(int t = 2; t < length + 1; ++t){
            for(int i = 0; i < length - t + 1; ++i){
                for(int j = 0; j < length - t + 1; ++j){
                    for(int k = 1; k < t; ++k){
                        if((table[k][i][j] && table[t-k][i+k][j+k]) || 
                        (table[k][i][j+t-k] && table[t-k][i+k][j])){
                            table[t][i][j] = true;
                            break;
                        }
                    }
                }
            }
        }
        return table[length][0][0];
    }
    bool doHelper(string& s, int ss, int se, string& t, int ts, int te){
        if (s.substr(ss, se) == t.substr(ts, te)) return true;
        if (se == 1) return false;
        for (int i = 1; i < se; ++i){
            if (doHelper(s, ss, i, t, ts, i) && doHelper(s, ss + i, se - i, t, ts + i, te - i)) return true;
            if (doHelper(s, ss, i , t, ts + te - i, i) && doHelper(s, ss + i, se - i, t, ts, te - i)) return true;
        }
        return false;
    }
};
