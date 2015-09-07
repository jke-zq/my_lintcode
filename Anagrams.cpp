class Solution {
public:    
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    vector<string> anagrams(vector<string> &strs) {
        // write your code here
        unordered_map<string, int> map;
        for (auto s : strs){
            sort(s.begin(), s.end());
            ++map[s];
        }
        vector<string> ret;
        for (const auto& s : strs){
            string sorted_s(s);
            sort(sorted_s.begin(), sorted_s.end());
            if (map[sorted_s] > 1)
                ret.emplace_back(s);
        }
        return ret;
    }
};

