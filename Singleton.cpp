class Solution {
public:
    /**
     * @return: The same instance of this class every time
     */
    static Solution* getInstance() {
        // write your code here
        //copy the answer.
        static Solution *instance = new Solution();
        return instance;
    }
    
    Solution(const Solution&) = delete;
    Solution& operation(const Solution&) = delete;
private:
    Solution(){};
    ~Solution(){};
};
