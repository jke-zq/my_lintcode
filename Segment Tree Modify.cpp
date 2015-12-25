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
     *@param root, index, value: The root of segment tree and 
     *@ change the node's value with [index, index] to the new given value
     *@return: void
     */
    void modify(SegmentTreeNode *root, int index, int value) {
        // write your code here
        // doModify(root, index, value);
        if (!root || root->start > index || root->end < index)
        {
            return;
        }
        if (root->start == root->end && root->start == index)
        {
            root->max = value;
            return;
        }
        
        modify(root->left, index, value);
        modify(root->right, index, value);
        
        int left_max = root->left == nullptr ? INT_MIN : root->left->max;
        int right_max = root->right == nullptr ? INT_MIN : root->right->max;
        root->max = max(left_max, right_max);
        return;
    }
    int doModify(SegmentTreeNode *root, int index, int value)
    {
        //root nerver should be null.
        if (!root || root->start > index || root->end < index)
        {
            return root->max;
        }
        if (root->start == root->end && root->start == index)
        {
            root->max = value;
            return value;
        }
        else
        {
            int maxValue = doModify(root->left, index, value);
            maxValue = max(maxValue, doModify(root->right, index, value));
            root->max = maxValue;
            return maxValue;
            
        }
    }
};