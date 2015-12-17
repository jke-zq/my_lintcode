/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 */
class Solution {
public:
    /**
     * @param intervals: interval list.
     * @return: A new interval list.
     */
    vector<Interval> merge(vector<Interval> &intervals) {
        // write your code here
        //sort
        if (intervals.empty())
        {
            return intervals;
        }
        sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b){
            return a.start < b.start;
        });
        vector<Interval> ret = {intervals[0]};
        for (int i = 1; i < intervals.size(); ++i)
        {
            Interval &pre = ret.back();
            if (intervals[i].start <= pre.end)
            {
                pre.end = max(intervals[i].end, pre.end);
            }
            else
            {
                ret.emplace_back(intervals[i]);
            }
        }
        return ret;
    }
};