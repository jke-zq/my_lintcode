class Solution{
public:
    /**
     * @param colors: A list of integer
     * @param k: An integer
     * @return: nothing
     */    
    void sortColors2(vector<int> &colors, int k) {
        // write your code here
        //using the colors to store the counts of colors
        for (int i = 0; i < colors.size(); ++i)
        {
            if (colors[i] > 0)
            {
                int pos = colors[i] - 1;
                if (colors[pos] <= 0)
                {
                    --colors[pos];
                    colors[i] = 0;
                }
                else
                {
                    colors[i] = colors[pos];
                    colors[pos] = -1;
                    --i;
                }
            }
        }
        
        for (int i = colors.size() - 1, pos = k - 1; pos >= 0; --pos)
        {
            while (colors[pos] < 0)
            {
                ++colors[pos];
                colors[i] = pos + 1;
                --i;
            }
        }
 
    }
};