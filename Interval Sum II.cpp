class SegmentTreeSumNode {
public:
    int start, end;
    long long sum;
    SegmentTreeSumNode *left, *right;
    SegmentTreeSumNode(int start, int end)
    {
        this->start = start;
        this->end = end;
        this->sum = sum;
        this->left = this->right = nullptr;
    }
};
class Solution {
private:
    SegmentTreeSumNode *root_;
public:
    /* you may need to use some attributes here */
    

    /**
     * @param A: An integer vector
     */
    Solution(vector<int> A) {
        // write your code here
        root_ = build(0, A.size() - 1, A);
    }
    
    /**
     * @param start, end: Indices
     * @return: The sum from start to end
     */
    long long query(int start, int end) {
        // write your code here
        return query(start, end, root_);
    }
    
    long long query(int start, int end, SegmentTreeSumNode *node)
    {
        if (!node || node->start > end || node->end < start)
        {
            return 0L;
        }
        else if (node->start >= start && node->end <= end)
        {
            return node->sum;
        }
        else
        {
            long long left = query(start, end, node->left);
            long long right = query(start, end, node->right);
            return left + right;
        }
    }
    /**
     * @param index, value: modify A[index] to value.
     */
    void modify(int index, int value) {
        // write your code here
        modify(index, value, root_);
    }
    
    long long modify(int index, int value, SegmentTreeSumNode *node)
    {
        if (!node || node->start > index || node->end < index)
        {
            return node ? node->sum : 0;
        }
        else if (node->start == index && node->end == index)
        {
            node->sum = value;
            return value;
        }
        else
        {
            long long left = modify(index, value, node->left);
            long long right = modify(index, value, node->right);
            node->sum = left + right;
            return node->sum;
        }
    }
    
    SegmentTreeSumNode *build(int start, int end, vector<int> &A)
    {
        if (start > end)
        {
            return nullptr;
        }
        else
        {
            SegmentTreeSumNode *root = new SegmentTreeSumNode(start, end);
            if (start == end)
            {
                root->sum = A[start];
                return root;
            }
            else
            {
                int mid = start + (end - start) / 2;
                root->left = build(start, mid, A);
                root->right = build(mid + 1, end, A);
                long long left_sum = root->left ? root->left->sum : 0;
                long long right_sum = root->right ? root->right->sum : 0;
                root->sum = left_sum + right_sum;
                return root;
            }
        }
    }
};
