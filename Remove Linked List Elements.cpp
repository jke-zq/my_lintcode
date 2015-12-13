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
     * @param val an integer
     * @return a ListNode
     */
    ListNode *removeElements(ListNode *head, int val) {
        // Write your code here
        ListNode dummy(INT_MIN);
        dummy.next = head;
        ListNode *pre = &dummy;
        ListNode *post = head;
        while (post)
        {
            if (post->val == val)
            {
                auto tmp = post;
                post = post->next;
                pre->next = post;
                delete tmp;
            }
            else
            {
                post = post->next;
                pre = pre->next;
            }
        }
        return dummy.next;
        
    }
};