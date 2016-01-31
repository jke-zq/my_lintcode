/**
 * Definition of ArrayReader:
 * 
 * class ArrayReader {
 * public:
 *     int get(int index) {
 *          // return the number on given index, 
 *          // return -1 if index does not exist.
 *     }
 * };
 */
class Solution {
public:
    /**
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return: An integer which is the first index of target.
     */
    int searchBigSortedArray(ArrayReader *reader, int target) {
        // write your code here
        int k = 1;
        int va = reader->get(k);
        while (va != -1 && va < target)
        {
            k *= 2;
            va = reader->get(k);
        }
        int left = 0;
        int right = k;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int val = reader->get(mid);
            if (val == -1 || val > target)
            {
                right = mid - 1;
            }
            else if (val < target)
            {
                left = mid + 1;
            }
            else
            {
                while (reader->get(mid) == target)
                {
                    --mid;
                }
                return mid + 1;
            }
        }
        return -1;
        
    }
};