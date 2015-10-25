class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number occurs more than 1/3.
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int k = 3;
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
        for (auto& it : hash){
            it.second = 0;
        }
        for (auto& i : nums){
            auto it = hash.find(i);
            if (it != hash.end()){
                ++it->second;
            }
        }
        int n = nums.size();
        vector<int> res;
        for (const pair<int, int>& it : hash){
            if (it.second > static_cast<double>(n) / k){
                res.emplace_back(it.first);
            }
        }
        return res[0];
    }
};

