class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        // write your code here
        if(s.length() != t.length()) return false;
        unordered_map<char, int> map;
        for(auto& c : s){
            ++map[c];
        }
        for(auto& c : t){
            --map[c];
            if(map[c] < 0) return false;
        }
        return true;
    }
};
