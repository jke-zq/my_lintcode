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
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) {
        // write your code here
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        if (!head) return head;
        while (head->next){
            if (head->val == head->next->val){
                auto need_to_removed = head->next;
                head->next = need_to_removed->next;
                delete need_to_removed;
            }else{
                head = head->next;
            }
        }
        return dummy->next;
    }
};
