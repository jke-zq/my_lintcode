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
     * @return: The head of linked list.
     */
    ListNode *insertionSortList(ListNode *head) {
        // write your code here
        ListNode dummy(INT_MIN);
        dummy.next = head;
        ListNode *node = head->next;
        ListNode *pre = head;
        while (node)
        {
            ListNode *tmp = &dummy;
            while (tmp->next != node && tmp->next->val < node->val)
            {
                tmp = tmp->next;
            }
            if (tmp->next != node)
            {
                ListNode *node_next = node->next;
                node->next = tmp->next;
                tmp->next = node;
                pre->next = node_next;
                node = node_next;
            }
            else
            {
                node = node->next;
                pre = pre->next;
            }
        }
        return dummy.next;
    }
};