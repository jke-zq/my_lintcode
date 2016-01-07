class Solution {
public:
    /**
     * @param buildings: A list of lists of integers
     * @return: Find the outline of those buildings
     */
    vector<vector<int> > buildingOutline(vector<vector<int> > &buildings) {
        // write your code here
        map<int, vector<int>> point_heights;//need points ordered by asc
        for (const auto b : buildings)
        {
            point_heights[b[0]].emplace_back(b[2]);
            point_heights[b[1]].emplace_back(0 - b[2]);
        }
        
        vector<vector<int>> ret;
        int curr_start = -1;
        int curr_height = 0;
        map<int, int> heights;//ordered by key asc
        for (auto & kvp : point_heights)
        {
            int p = kvp.first;
            auto &hs = kvp.second;
            for (auto h : hs)
            {
                if (h < 0)
                {
                    h *= -1;
                    --heights[h];
                    if (heights[h] == 0)
                    {
                        heights.erase(h);
                    }
                }
                else
                {
                    ++heights[h];
                }
            }
            
            if (heights.empty() || curr_height != heights.crbegin()->first)
            {
                if (curr_height > 0)
                {
                    ret.emplace_back(move(vector<int>{curr_start, p, curr_height}));
                }
                curr_start = p;
                curr_height = heights.empty() ? 0 : heights.crbegin()->first;
            }
        }
        return ret;
    }
};