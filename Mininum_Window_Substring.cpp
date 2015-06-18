/**
*NOTE:
*     Good solution that I cant write.
*     1.find the valid window and maintain the constraint.
*     2.two hashMap and two points is the result of deep understanding the question.
*/
class Solution {
public:    
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    string minWindow(string &source, string &target) {
        // write your code here
        unordered_map<char, int> needToFound;
        unordered_map<char, int> hasFound;
        int s = 0;
        int e = 0;
        int count = 0;
        string result("");
        for(auto& c : target){
            if(needToFound.find(c) == needToFound.end()){
                hasFound.emplace(c, 0);
                needToFound.emplace(c, 1);
            }else{
                ++needToFound[c];
            }
        }
        for(auto& c : source){
            ++e;
            if(needToFound.find(c) == needToFound.end()) continue;
            ++hasFound[c];
            if(count < target.size() && needToFound[c] >= hasFound[c]) ++count;
            if(count == target.size()){
                while(s <= e){
                    if(needToFound.find(source[s]) == needToFound.end()){
                        ++s;
                        continue;
                    }
                    if(hasFound[source[s]] > needToFound[source[s]]){
                        --hasFound[source[s]];
                        ++s;
                    }else{
                        break;
                    }
                }
                if(result == "" || result.size() > e - s) result = source.substr(s, e - s);
            }

        }
        return result;
    }
};

