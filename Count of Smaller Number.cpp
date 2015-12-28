
class Solution {
public:
   /**
     * @param A: An integer array
     * @return: The number of element in the array that 
     *          are smaller that the given integer
     */
    // class SegmentTreeNode {
    // public:
    //     int start, end, count;
    //     SegmentTreeNode *left, *right;
    //     SegmentTreeNode(int start, int end, int count)
    //     {
    //         this->start = start;
    //         this->end = end;
    //         this->count = count;
    //         this->left = nullptr;
    //         this->right = nullptr;
    //     }
    // };
    vector<int> countOfSmallerNumber(vector<int> &A, vector<int> &queries) {
        // write your code here
        vector<int> ret;
        sort(A.begin(), A.end());
        SegmentTreeNode *root = build(A, 0, A.size() - 1);
        for (const auto &q : queries)
        {
            ret.emplace_back(query(A, root, q));
        }
        return ret;
    }
    
    SegmentTreeNode *build(vector<int> &A, int start, int end)
    {
        if (start > end)
        {
            return nullptr;
        }
        else
        {
            SegmentTreeNode *root = new SegmentTreeNode(start, end, 0);
            if (start == end)
            {
                root->count = 1;
                return root;
            }
            else
            {
                int mid = start + (end - start) / 2;
                root->left = build(A, start, mid);
                root->right = build(A, mid + 1, end);
                int left_count = root->left == nullptr ? 0 : root->left->count;
                int right_count = root->right == nullptr ? 0 : root->right->count;
                root->cunt = left_count + right_count;
                return root;
            }
        }
    }
    
    int query(vector<int> &A, SegmentTreeNode *root, int q)
    {
        if (!root)
        {
            return 0;
        }
        else
        {
            if (q <= A[root->start])
            {
                return 0;
            }
            else if (q > A[root->end])
            {
                return root->count;
            }
            else
            {
                int left = query(A, root->left, q);
                int right = query(A, root->right, q);
                return left + right;
            }
        }
    }
};