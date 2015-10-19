class Solution {
public:
    /**
     * @param gas: a vector of integers
     * @param cost: a vector of integers
     * @return: an integer 
     */
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // write your code here
        
        // int left = 0;
        // int start = 0;
        // int walked = 0;
        // int gas_len = gas.size();
        // while (walked < gas_len){
        //     left += gas[(start + walked) % gas_len];
        //     if (left < cost[(start + walked) % gas_len] && start < gas_len - 1){
        //         left -=gas[start];
                
        //         if (walked){
        //             left += cost[start];
        //             left -= gas[(start + walked) % gas_len];
        //             --walked;
        //         }
                
        //         ++start;
        //     }else {
        //         left -= cost[(start + walked) % gas_len];
        //         ++walked;
        //     }
        // }
        // return left < 0 ? -1 : start;
        //good solution
        int total_sum = 0;
        int current_sum = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); ++i){
            total_sum += gas[i] - cost[i];
            current_sum += gas[i] - cost[i];
            if (current_sum < 0){
                current_sum = 0;
                start = i + 1;//from i + 1 to find the start
            }
        }
        if (total_sum >= 0){
            return start;
        }
        return -1;
    }
};
