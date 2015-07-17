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
     *@param root, start, end: The root of segment tree and 
     *                         an segment / interval
     *@return: The maximum number in the interval [start, end]
     */
    int query(SegmentTreeNode *root, int start, int end) {
        // write your code here
        // if(root->start == start && root->end == end){
        //     return root->max;
        // }
        // SegmentTreeNode* left = root->left;
        // SegmentTreeNode* right = root->right;
        // if(end < right->start){
        //     return query(left, start, end);
        // }else if(start > left->end){
        //     return query(right, start, end);
        // }else{
        //     return max(query(left, start, left->end), query(right, right->start, end));
        // }
        //good codes
        if(root == nullptr || root->end < start || root->start > end){
            return INT_MIN;
        }
        if(root->end <= end && root->start >= start){
            return root->max;
        }
        int left = query(root->left, start, end);
        int right = query(root->right, start, end);
        return max(left, right);
    }
};
