
/**
*NOTE:
*     get the max points that on the line with someone point. And do this one by one.
*     careful with the same point.x value and y value are the same.
**/

/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
#include <cfloat>
class Solution {
public:
    /**
     * @param points an array of point
     * @return an integer
     */
    int maxPoints(vector<Point>& points) {
        // Write your code here
        int size = points.size();
        if(size == 0) return 0;
        int maxpoints = 0;
        for(int i = 0; i < size; ++i){
            unordered_map<float, int> map;
            int same = 1;
            for(int j = i+1; j < size; ++j){
                if(points[i].x == points[j].x && points[i].y == points[j].y){
                    ++same;
                }else{
                    float slope = FLT_MAX;
                    if(points[i].x != points[j].x){
                        slope = (points[i].y-points[j].y) * 1.0f / (points[i].x-points[j].x);
                    }
                    ++map[slope];
                    
                }
            }
            int result = same;
            for(auto& v:map)
                result = result > same + v.second ? result : same + v.second;
            maxpoints = max(maxpoints, result);
        }

        return maxpoints;
    }
};
