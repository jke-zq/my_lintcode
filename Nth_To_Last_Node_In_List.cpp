/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode *nthToLast(ListNode *head, int n) {
        // write your code here
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* front = dummy;
        ListNode* back = dummy;
        while(n-- > 0) front = front->next;
        while(front){
            back = back->next;
            front = front->next;
        }
        return back;
    }
};
