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
     * @return: The head of linked list.
     */
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        // write your code here
        //maybe the n is larger than the length of head
        auto dummy = new ListNode(-1);
        dummy->next = head;
        auto pre = dummy;
        int length = 0;
        while (pre->next != nullptr){
            ++length;
            pre = pre->next;
        }
        n = n % length;
        n = n == 0 ? length : n;
        pre = dummy;
        while (n > 0){
            --n;
            pre = pre->next;
        }
        auto next = dummy;
        while (pre->next != nullptr){
            pre = pre->next;
            next = next->next;
        }
        //remove node
        auto node_to_delete = next->next;
        next->next = node_to_delete->next;
        //delete the removed node
        delete node_to_delete;
        return dummy->next;
    }
};



