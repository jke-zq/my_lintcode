class Solution {
public:
    /**
     * @param numbers: Give an array numbersbers of n integer
     * @param target: you need to find four elements that's sum of target
     * @return: Find all unique quadruplets in the array which gives the sum of 
     *          zero.
     */
    vector<vector<int> > fourSum(vector<int> nums, int target) {
        // write your code here
        unordered_map<int, vector<pair<int, int>>> table;
        sort(nums.begin(), nums.end());
        int length = nums.size();
        for (int i = 0; i < length; ++i){
            for (int j = i + 1; j < length; ++j){
                bool is_duplicate = false;
                for (auto& p : table[nums[i] + nums[j]]){
                    if (p.first == i){
                        is_duplicate = true;
                        break;
                    }
                }
                if (!is_duplicate){
                    table[nums[i] + nums[j]].emplace_back(pair<int,int>(i, j));
                }
            }
        }
        unordered_set<string> check_unique;
        vector<vector<int>> ret;
        for (int i = 0; i < length; ++i){
            for (int j = i + 1; j < length; ++j){
                int diff = target - nums[i] - nums[j];
                if (table.find(diff) != table.end()){
                    for (auto& p : table[diff]){
                        if (j < p.first){
                            vector<int> tmp = {nums[i], nums[j], nums[p.first], nums[p.second]};
                            if (check_unique.emplace(vector_to_string(tmp)).second){
                                ret.emplace_back(tmp);
                            }
                        }
                    }
                }
            }
        }
        
        return ret;
    }
    string vector_to_string(vector<int> v){
        string ret;
        for (auto& i : v){
            ret += i;
            ret += ' ';
        }
        return ret;
    }
};

