class Solution {
public:
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true of false.
     */
    bool isInterleave(string s1, string s2, string s3) {
        // write your code here
        if(s1.length() + s2.length() != s3.length()){
            return false;
        }
        if(s1.length() > s2.length()){
            return isInterleave(s2, s1, s3);
        }
        vector<vector<int>> table(2, vector<int>(s1.length() + 1, false));
        table[0][0] = true;
        for(int i = 0; i < s1.length(); ++i){
            if(s1[i] == s3[i]) table[0][i+1] = true;
            else break;
        }
        for(int i = 0; i < s2.length(); ++i){
            table[(i+1)%2][0] = table[i%2][0] && s2[i] == s3[i];
            for(int j = 0; j < s1.length(); ++j){
                table[(i+1)%2][j+1] = (table[i%2][j+1] && s2[i] == s3[i+j+1]) ||
                (table[(i+1)%2][j] && s1[j] == s3[i+j+1]);
            }
        }
        return table[s2.length()%2][s1.length()];
    }
};
