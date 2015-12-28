class Solution {
public:
    /**
     * @param A: Given an integer array
     * @return: void
     */
    void heapify(vector<int> &A) {
        // write your code here
        for (int i = 0; i < A.size(); ++i)
        {
            int child = i;
            // while (1.0 * (child - 1) / 2 >= 0)
            // {
            //     int parent = (child - 1) / 2;
            //     if (A[child] < A[parent])
            //     {
            //         swap(A[parent], A[child]);
            //     }
            //     child = parent;
            // }
            while (1.0 * (child - 1) / 2 >= 0)
            {
                int parent = (child - 1) / 2;
                if (A[child] < A[parent])
                {
                    swap(A[parent], A[child]);
                    child = parent;
                }
                else
                {
                    break;
                }
                
            }
        }
    }
};