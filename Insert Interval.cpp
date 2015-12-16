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
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        // write your code here

        for (int i = 0; i < intervals.size();)
        {
            if (intervals[i].start > newInterval.end)
            {
                intervals.emplace(intervals.begin() + i, newInterval);
                return intervals;
            }
            else if (intervals[i].end < newInterval.start)
            {
                ++i;
            }
            else
            {
                newInterval.start = min(intervals[i].start, newInterval.start);
                newInterval.end = max(intervals[i].end, newInterval.end);
                //delete the ith element of intervals
                intervals.erase(intervals.begin() + i);
            }
        }
        intervals.emplace_back(newInterval);
        return intervals;
    }
};