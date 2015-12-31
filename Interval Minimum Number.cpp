/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 */
class SegmentTreeMiniNode {
public:
    int start, end, mini;
    SegmentTreeMiniNode *left, *right;
    SegmentTreeMiniNode(int start, int end)
    {
        this->start = start;
        this->end = end;
        this->mini = INT_MIN;
        this->left = this->right = nullptr;
    }
};
class Solution { 
private:
    SegmentTreeMiniNode *root_;
public:
    /**
     *@param A, queries: Given an integer array and an query list
     *@return: The result list
     */
    vector<int> intervalMinNumber(vector<int> &A, vector<Interval> &queries) {
        // write your code here
        root_ = build(0, A.size() - 1, A);
        vector<int> ret;
        for (const auto &interval : queries)
        {
            ret.emplace_back(query(interval.start, interval.end, root_));
        }
        return ret;
    }
    int query(int start, int end, SegmentTreeMiniNode *root)
    {
        if (!root || root->start > end || root->end < start)
        {
            return INT_MAX;
        }
        else
        {
            if (start <= root->start && end >= root->end)
            {
                return root->mini;
            }
            else
            {
                return min(query(start, end, root->left), query(start, end, root->right));
            }
        }
    }
    SegmentTreeMiniNode *build(int start, int end, vector<int> &A)
    {
        if (start > end)
        {
            return nullptr;
        }
        else
        {
            SegmentTreeMiniNode *root = new SegmentTreeMiniNode(start, end);
            if (start == end)
            {
                root->mini = A[start];
                return root;
            }
            else
            {
                int mid = start + (end - start) / 2;
                root->left = build(start, mid, A);
                root->right = build(mid + 1, end, A);
                int left_mini = root->left ? root->left->mini : INT_MAX;
                int right_mini = root->right ? root->right->mini : INT_MAX;
                root->mini = min(left_mini, right_mini);
                return root;
            }
        }
    }
};