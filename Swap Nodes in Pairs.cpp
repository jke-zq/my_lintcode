/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head a ListNode
     * @return a ListNode
     */
    ListNode* swapPairs(ListNode* head) {
        // Write your code here
        ListNode dummy(INT_MIN);
        dummy.next = head;
        auto pre = &dummy;
        while (pre->next && pre->next->next)
        {
            auto first = pre->next;
            auto second = pre->next->next;
            pre->next = second;
            first->next = second->next;
            second->next = first;
            pre = pre->next->next;
        }
        return dummy.next;
    }
};