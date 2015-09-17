class Solution {
public:    
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    vector<vector<int> > threeSum(vector<int> &nums) {
        // write your code here
        // sort(nums.begin(), nums.end());
        // vector<vector<int>> ret;
        // int length = nums.size();
        // int start, end;
        // for (int i = 0; i < length; ++i){
        //     if (i >  0 && nums[i] == nums[i - 1]) continue;
        //     start = i + 1;
        //     end = length - 1;
        //     while (start < end){
        //         if (nums[start] + nums[end] + nums[i] == 0){
        //             ret.emplace_back(vector<int>{nums[i], nums[start], nums[end]});
        //             ++start;
        //             --end;
        //             while (start < end && nums[start] == nums[start - 1]) ++start;
        //             while (end > start && nums[end] == nums[end + 1]) --end;
                    
        //         }else if (nums[start] + nums[end] + nums[i] > 0){
        //             --end;
        //         }else{
        //             ++start;
        //         }
        //     }
        // }
        // return ret;
        // better codes of the same solution
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        int length = nums.size();
        int start, end;
        for (int i = 0; i < length; ++i){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            start = i + 1;
            end = length - 1;
            while (start < end){
                if (start > i + 1 && nums[start] == nums[start - 1]){
                    ++start;
                }else if (end < length - 1 && nums[end] == nums[end + 1]){
                    --end;
                }else{
                    const auto sum = nums[i] + nums[end] + nums[start];
                    if (sum > 0){
                        --end;
                    }else if (sum < 0){
                        ++start;
                    }else{
                        ret.emplace_back(vector<int>{nums[i], nums[start], nums[end]});
                        ++start;
                        --end;
                    }
                }
                
            }
        }
        return ret;
    }
};

