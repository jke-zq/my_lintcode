class Solution {
public:
    /**
     * @param matrix: a matrix of integers
     * @param k: an integer
     * @return: the kth smallest number in the matrix
     */
    struct Compare{
        bool operator()(const pair<int, pair<int, int>> a, const pair<int, pair<int, int>> b){
            return a.first > b.first;
        }
    };
    int kthSmallest(vector<vector<int> > &matrix, int k) {
        // write your code here
        if (matrix.size() < matrix[0].size())
        {
            return horizontal(matrix, k);
        }
        else
        {
            return vertical(matrix, k);
        }
    }
    int horizontal(const vector<vector<int>> &matrix, int k)
    {
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, Compare> min_heap;
        for (int i = 0; i < min(k, static_cast<int>(matrix.size())); ++i)
        {
            min_heap.emplace(pair<int, pair<int, int>>{matrix[i][0], {i, 0}});
        }
        
        while (!min_heap.empty() && k--)
        {
            if (k == 0)
            {
                return min_heap.top().first;
            }
            int i = min_heap.top().second.first;
            int j = min_heap.top().second.second;
            min_heap.pop();
            if (j + 1 < matrix[0].size())
            {
                min_heap.emplace(pair<int, pair<int, int>>{matrix[i][j + 1], {i, j + 1}});
            }
        }
        
        return matrix[matrix.size() - 1][matrix[0].size() - 1];
    }
    int vertical(const vector<vector<int>> &matrix, int k)
    {
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, Compare> min_heap;
        for (int i = 0; i < min(static_cast<int>(matrix[0].size()), k); ++i)
        {
            min_heap.emplace(pair<int, pair<int, int>>{matrix[0][i], {0, i}});
        }
        
        while (!min_heap.empty() && k--)
        {
            if (k == 0)
            {
                return min_heap.top().first;
            }
            int i = min_heap.top().second.first;
            int j = min_heap.top().second.second;
            min_heap.pop();
            if (i + 1 < matrix.size())
            {
                min_heap.emplace(pair<int, pair<int, int>>{matrix[i + 1][j], {i + 1, j}});
            }
            
        }
        
        return matrix[matrix.size() - 1][matrix[0].size() - 1];
        
    }
};