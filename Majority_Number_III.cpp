class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums, int k) {
        // write your code here
        //if (occurs / n > 1 / k), then (occusrs - 1)/(n - k) > 1/k
        unordered_map<int, int> hash;
        for (auto& i : nums){
            ++hash[i];
            if (hash.size() == k){
                auto it = hash.begin();
                while (it != hash.end()){
                    if (--it->second == 0){
                        hash.erase(it++);
                    }else{
                        ++it;
                    }
                }
            }
        }
        
        //reset to zero and recount the occurs
        for (auto& it : hash){
            it.second = 0;
        }
        
        for (auto& i : nums){
            auto it = hash.find(i);
            if (it != hash.end()){
                ++it->second;
            }
        }
        //to judge the occurs if > 1/k
        int n = nums.size();
        vector<int> res;
        for (const pair<int, int>& it : hash){
        // for (auto& it : hash){
            if (it.second > static_cast<double>(n) / k){
                res.emplace_back(it.first);
            }
        }
        return res[0];
    }
};

