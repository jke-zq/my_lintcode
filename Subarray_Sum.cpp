class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        // write your code here
        // int n = nums.size();
        // for (int i = 0; i < n; ++i){
        //     int sum = 0;
        //     for (int j = i; j < n; ++j){
        //         sum += nums[j];
        //         if (sum == 0){
        //             // return vector<int>{i, j};
        //             return {i,j};
        //         }
        //     }
        // }
        // // return vector<int>();
        // return {};
        
        //other better solution
        unordered_map<int, int> table;
        table[0] = -1;
        for (int i = 0, sum = 0; i < nums.size(); ++i){
            sum += nums[i];
            if (!table.emplace(sum, i).second){
                return {table[sum] + 1, i};
            }
        }
        return {};
    }
};
