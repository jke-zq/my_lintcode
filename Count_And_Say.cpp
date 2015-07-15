class Solution {
public:
    /**
     * @param n the nth
     * @return the nth sequence
     */
    string countAndSay(int n) {
        // Write your code here--ugly
        // if(n == 1) return "1";
        // vector<int> s;
        // s.emplace_back(1);
        // int count = 0;
        // int tag = 0;
        // int times = 0;
        // vector<int> pre;
        // while(times < n - 1){
        //     ++times;
        //     count = 0;
        //     for(auto i : s){
        //         if(count == 0){
        //             tag = i;
        //             ++count;
        //         }else{
        //             if(tag == i){
        //                 ++count;
        //             }else{
        //                 pre.emplace_back(count);
        //                 pre.emplace_back(tag);
        //                 count = 1;
        //                 tag = i;
        //             }
        //         }
        //     }
        //     pre.emplace_back(count);
        //     pre.emplace_back(tag);
        //     s = move(pre);
        //     pre.clear();
            
        // }
        // string result;
        // for(auto i : s){
        //     result += to_string(i); 
        // }
        // return result;
        // write your code here
        string s{"1"};
        for(int i = 0; i < n - 1; ++i){
            s = move(getNext(s));
        }
        return s;
    }
    string getNext(string s){//const string&
        stringstream sst;
        for(int i = 0; i < s.length(); ++i){
            int cnt = 1;
            while(i < s.length() - 1 && s[i] == s[i+1]){
                ++cnt;
                ++i;
            }
            sst << cnt << s[i];
        }
        return sst.str();
    }
};
