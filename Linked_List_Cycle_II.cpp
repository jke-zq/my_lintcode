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
     * @return: The node where the cycle begins. 
     *           if there is no cycle, return null
     */
    ListNode *detectCycle(ListNode *head) {
        // write your code here
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        ListNode *fast = dummy, *slow = dummy;
        while (fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow){
                //check the circle
                fast = dummy;
                while (slow != fast){
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return nullptr;
    }
};



