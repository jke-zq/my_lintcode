/**
*NOTE:
*    At first, its hard to me to understand the KMP. When I try to understand the algorithm at the second time, I feel better than ever.
*    And I will remember this fro a longger time.
*/

class Solution {
public:
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    int strStr(const char *source, const char *target) {
        // write your code here
        // if(source != nullptr && target != nullptr){
        //     const string ssr(source), stg(target);
        //     for(int i = 0; i < ssr.length() - stg.length() + 1; ++i){
        //         if(ssr.substr(i, stg.length()) == stg) return i;
        //     }
        // }
        // return -1;
        //solution II
        // if(source == nullptr) return target == nullptr ? -1 : -1;
        // if(target == nullptr) return source == nullptr ? -1 : -1;
        // if(target == nullptr || source == nullptr) return -1;
        // if(!*source) return !*target ? 0 : -1;
        // if(!*target) return 0;
        // while(*source){
        //     if(*source == *target){
        //         const char* t = target;
        //         const char* s = source;
        //         while(*s && *t && *s == *t){
        //             ++s;
        //             ++t;
        //         }
        //         if(!*t) return true;
        //     }
        //     ++source;
        // }
        // return -1;
        //kmp solution
        if(source != nullptr && target != nullptr){
            string src(source), tgt(target);
            //if()
            vector<int> dfa = getDFA(tgt);
            if(tgt.empty()) return 0;
            int j = -1;
            for(int i = 0; i < src.length(); ++i){
                while(j > -1 && tgt[j+1] != src[i])
                    j = dfa[j];
                if(tgt[j+1] == src[i])
                    ++j;
                if(j == tgt.length() - 1) return i - j;
            }
        }
        return -1;
    }
    vector<int> getDFA(const string& target){
        vector<int> dfa(target.length(), -1);
        int j = -1;
        for(int i = 1; i < target.length(); ++i){
            while(j > -1 && target[j+1] != target[i])
                j = dfa[j];
            if(target[j+1] == target[i])
                ++j;
            dfa[i] = j;
        return dfa;
        }
    }

};

