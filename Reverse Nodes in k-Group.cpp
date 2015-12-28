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
     * @param k an integer
     * @return a ListNode
     */
    ListNode *reverseKGroup(ListNode *head, int k) {
        // Write your code here
        ListNode dummy(INT_MIN);
        dummy.next = head;
        ListNode *h = &dummy;
        while (h)
        {
            ListNode *first = h;
            ListNode *last = first;
            int loops = k;
            while (last && loops > 0)
            {
                --loops;
                last = last->next;
            }
            if (!last)
            {
                return dummy.next;
            }
            else
            {
                ListNode *pre = first->next;
                h = pre;
                int loops = k;
                while (loops > 1)
                {
                    --loops;
                    ListNode *next = pre->next;
                    pre->next = last->next;
                    last->next = pre;
                    first->next = next;
                    pre = next;
                }
            }
            
        }
        return dummy.next;
        
    }
};