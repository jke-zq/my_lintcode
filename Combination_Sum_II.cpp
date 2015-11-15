class Solution {
public:
	/**
	 * @param num: Given the candidate numbers
	 * @param target: Given the target number
	 * @return: All the combinations that sum to target
	 */
    vector<vector<int>> combinationSum2(vector<int> &num, int target) {
        // write your code here
        vector<vector<int>> ret;
        int len = num.size();
        if (len == 0)
        {
            return ret;
        }
        sort(num.begin(), num.end());
        vector<int> tmp;
        doHelper(0, len, target, num, tmp, ret);
        return ret;
    }
    
private:
    void doHelper(int start, int len, int target, const vector<int> &num, vector<int> &tmp, vector<vector<int>> &ret)
    {
        if (target == 0)
        {
            ret.emplace_back(tmp);
            return;
        }
        for (int i = start; i < len; ++i)
        {
            if (num[i] > target)
            {
                break;
            }
            if (i > start && num[i] == num[i - 1])
            {
                continue;
            }
            tmp.emplace_back(num[i]);
            doHelper(i + 1, len, target - num[i], num, tmp, ret);
            tmp.pop_back();
            // doHelper(i + 1, len, target, num, tmp, ret);
        }
        
    }
};
