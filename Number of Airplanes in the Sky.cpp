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
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    struct Compare {
        bool operator()(const Interval &a, const Interval &b)
        {
            return a.start != b.start ? a.start < b.start : a.end < b.end;
        }
    };
    int countOfAirplanes(vector<Interval> &airplanes) {
        // write your code here
        size_t max_planes = 0;
        // int max_planes = 0;//error error: no matching function for call to ‘max(int&, std//::priority_queue, std::greater >::size_type)’
        priority_queue<int, vector<int>, greater<int>> min_heap;
        sort(airplanes.begin(), airplanes.end(), Compare());
        for (const auto &a : airplanes)
        {
            min_heap.emplace(a.end);
            while (min_heap.top() <= a.start)
            {
                min_heap.pop();
            }
            max_planes = max(max_planes, min_heap.size());
        }
        return max_planes;
    }
};