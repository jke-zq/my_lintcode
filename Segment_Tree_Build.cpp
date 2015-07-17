/**
 * Definition of SegmentTreeNode:
 * class SegmentTreeNode {
 * public:
 *     int start, end;
 *     SegmentTreeNode *left, *right;
 *     SegmentTreeNode(int start, int end) {
 *         this->start = start, this->end = end;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     *@param start, end: Denote an segment / interval
     *@return: The root of Segment Tree
     */
    SegmentTreeNode * build(int start, int end) {
        // write your code here
        if(start > end) return nullptr;
        SegmentTreeNode* root = new SegmentTreeNode(start, end);
        doBuild(root);
        return root;
    }
    void doBuild(SegmentTreeNode* node){
        if(node->start == node->end) return;
        SegmentTreeNode* left = new SegmentTreeNode(node->start, (node->start + node->end) / 2);
        SegmentTreeNode* right = new SegmentTreeNode((node->start + node->end) / 2 + 1, node->end);
        node->left = left;
        node->right = right;
        doBuild(left);
        doBuild(right);
        
    }
};
