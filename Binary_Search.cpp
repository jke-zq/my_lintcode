class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &array, int target) {
        // write your code here
        // if(array.size() > 0){
        //     int size = array.size();
        //     int start = 0;
        //     int end = size - 1;
        //     while(start <= end){
        //         int mid = start + (end - start) / 2;
        //         if(array[mid] > target){
        //             end = mid - 1;
        //         }else if(array[mid] < target){
        //             start = mid + 1;
        //         }else{
        //             while(mid > -1 && array[mid--] == target){
        //             }
        //             if(mid < 0) return 0;
        //             else return mid + 2;
        //         }

        //     }
        // }
        // return -1;
        int start = 0;
        int end = array.size();
        while(start < end){
            int mid = start + (end - start) / 2;
            if(array[mid] >= target)
                end = mid;
            else
                start = mid + 1;
        }
        if(start < array.size() && array[start] == target)
            return start;
        return -1;
    }
};
