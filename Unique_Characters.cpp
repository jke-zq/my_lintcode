class Solution {
public:
    /**
     * @param str: a string
     * @return: a boolean
     */
    bool isUnique(string &str) {
        // write your code here
        // int len = str.size();
        // for(int i = 0; i < len; ++i){
        //     for(int j = i + 1; j < len; ++j){
        //         if(str[i] == str[j]) return false;
        //     }
        // }
        // return true;
        unordered_map<char, int> map;
        for(auto& s : str){
            ++map[s];
            if(map[s] > 1) return false;
        }
        return true;
    }
};
