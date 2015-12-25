/**
 * Definition of SegmentTreeNode:
 * class SegmentTreeNode {
 * public:
 *     int start, end, max;
 *     SegmentTreeNode *left, *right;
 *     SegmentTreeNode(int start, int end, int max) {
 *         this->start = start;
 *         this->end = end;
 *         this->max = max;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     *@param A: a list of integer
     *@return: The root of Segment Tree
     */
    SegmentTreeNode * build(vector<int>& A) {
        // write your code here
        if (A.empty())
        {
            return nullptr;
        }
        return doBuild(0, A.size() - 1, A);
    }
    SegmentTreeNode *doBuild(int start, int end, vector<int> &A)
    {
        if (start == end)
        {
            return new SegmentTreeNode(start, start, A[start]);
        }
        SegmentTreeNode *node = new SegmentTreeNode(start, end, 0);
        int mid = start + (end - start) / 2;
        node->left = doBuild(start, mid, A);
        node->right = doBuild(mid + 1, end, A);
        node->max = max(node->left->max, node->right->max);
        return node;
        
    }
};