/**
 * class Comparator {
 *     public:
 *      int cmp(string a, string b);
 * };
 * You can use compare.cmp(a, b) to compare nuts "a" and bolts "b",
 * if "a" is bigger than "b", it will return 1, else if they are equal,
 * it will return 0, else if "a" is smaller than "b", it will return -1.
 * When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
*/
class Solution {
public:
    /**
     * @param nuts: a vector of integers
     * @param bolts: a vector of integers
     * @param compare: a instance of Comparator
     * @return: nothing
     */
    void sortNutsAndBolts(vector<string> &nuts, vector<string> &bolts, Comparator compare) {
        // write your code here
        quickSort(nuts, bolts, 0, nuts.size() - 1, compare);
    }
    
    void quickSort(vector<string> &nuts, vector<string> &bolts, int left, int right, Comparator &compare)
    {
        if (left < right)
        {
            default_random_engine gen((random_device())());
            uniform_int_distribution<int> dis(left, right);
            int pivot = dis(gen);
            pivot = partition(nuts, left, right, bolts[pivot], compare);
            partition(bolts, left, right, nuts[pivot], compare);
            quickSort(nuts, bolts, left, pivot, compare);
            quickSort(nuts, bolts, pivot + 1, right, compare);
        }
    }
    
    int partition(vector<string> &arr, int left, int right, const string &pivot, Comparator &compare)
    {
        for (int i = left; i < right;)
        {
            if (compare.cmp(arr[i], pivot) == -1 || (compare.cmp(arr[i], pivot) == 2 && compare.cmp(pivot, arr[i]) == 1))
            {
                swap(arr[left], arr[i]);
                ++left, ++i;
            }
            else if (compare.cmp(arr[i], pivot) == 1 || (compare.cmp(arr[i], pivot) == 2 && compare.cmp(pivot, arr[i]) == -1))
            {
                ++i;
            }
            else
            {
                swap(arr[i], arr[right]);
            }
        }
        swap(arr[left], arr[right]);
        return left;
    }
};