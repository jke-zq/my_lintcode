class Solution {
public:
    /*
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    long long kthPrimeNumber(int k) {
        // write your code here
        //DP solution: O(k)
        // vector<long long> numbers(k + 1, 0);
        // int indexfor3 = 0, indexfor5 = 0, indexfor7 = 0;
        // numbers[0] = 1;
        // for (int i = 1; i <= k; ++i)
        // {
        //     numbers[i] = min(min(numbers[indexfor3] * 3, numbers[indexfor5] * 5), numbers[indexfor7] * 7);
        //     if (numbers[i] == numbers[indexfor3] * 3)
        //     {
        //         ++indexfor3;
        //     }
        //     if (numbers[i] == numbers[indexfor5] * 5)
        //     {
        //         ++indexfor5;
        //     }
        //     if (numbers[i] == numbers[indexfor7] * 7)
        //     {
        //         ++indexfor7;
        //     }
        // }
        // return numbers[k];
        
        //priority queue:O(k(logk))
        priority_queue<long long, vector<long long>, greater<long long>> que;
        que.emplace(3);
        que.emplace(5);
        que.emplace(7);
        long long min_cur;
        while (k-- > 0)
        {
            min_cur = que.top();
            que.pop();
            if (min_cur % 3 == 0)
            {
                que.emplace(min_cur * 3);
            }
            else if (min_cur % 5 == 0)
            {
                que.emplace(min_cur * 3);
                que.emplace(min_cur * 5);
            }
            else if (min_cur % 7 == 0)
            {
                que.emplace(min_cur * 3);
                que.emplace(min_cur * 5);
                que.emplace(min_cur * 7);
            }
        }
        return min_cur;
    }
};