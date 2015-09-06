class Solution {
public:
    /**
     * @param s a string
     * @return an integer
     */
    int minCut(string s) {
        // write your code here
        vector<vector<bool>> is_palindrome(s.size(), vector<bool>(s.size(), false));
        vector<int> T(s.size() + 1);
        //good init way and important to init -1 for the last.
        iota(T.rbegin(), T.rend(), -1);
        for (int i = s.size() - 1; i > -1; --i){
            for (int j = i; j < s.size(); ++j){
                if (s[i] == s[j] && (j - i < 2 || is_palindrome[i + 1][j - 1])){
                    is_palindrome[i][j] = true;
                    T[i] = min(T[i], 1 + T[j + 1]);
                }
            }
        }
        return T[0];
    }
};


