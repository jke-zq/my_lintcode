class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); ++i){
            map[nums[i]] = i + 1;
        }
        
        vector<int> ret;
        for (int i = 0; i < nums.size(); ++i){
            if (map.find(target - nums[i]) != map.end()){
                ret = {i + 1, map[target - nums[i]]};
                return ret;
            }
        }
        return {};
    }
};

